(() => {
  const intervalEl = document.getElementById("interval");
  const statusEl = document.getElementById("status");
  const lastPriceEl = document.getElementById("last-price");
  const changeEl = document.getElementById("change");
  const coverageEl = document.getElementById("coverage");
  const cutoverEl = document.getElementById("cutover");
  const spliceErrEl = document.getElementById("splice-err");
  const sourcesEl = document.getElementById("sources");
  const chartEl = document.getElementById("chart");
  const tooltipEl = document.getElementById("tooltip");
  const pinBadge = document.getElementById("ohlc-pin");
  const denomButtons = document.querySelectorAll("[data-denom]");
  const zoomBtn = document.getElementById("zoom-splice");

  const legend = {
    date: document.getElementById("ohlc-date"),
    o: document.getElementById("ohlc-o"),
    h: document.getElementById("ohlc-h"),
    l: document.getElementById("ohlc-l"),
    c: document.getElementById("ohlc-c"),
    chg: document.getElementById("ohlc-chg"),
    amp: document.getElementById("ohlc-amp"),
    v: document.getElementById("ohlc-v"),
    src: document.getElementById("ohlc-src"),
  };

  const SRC_LABEL = { mkr: "MKR 换算", sky: "SKY 实盘", splice: "拼接根" };

  let denomination = "sky";
  let chart;
  let candleSeries;
  let volumeSeries;
  let lastData = null;
  let byTime = new Map();
  let indexByTime = new Map();
  let pinnedTime = null;

  function fmtTime(ms, interval) {
    const iso = new Date(ms).toISOString();
    if (interval === "1d" || interval === "1w" || interval === "1M") {
      return iso.slice(0, 10) + " UTC";
    }
    return iso.slice(0, 16).replace("T", " ") + " UTC";
  }

  function fmtPrice(value, denom) {
    if (value == null || Number.isNaN(value)) return "—";
    if (denom === "sky") return value.toFixed(6);
    return value.toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  function fmtPct(value) {
    if (value == null || Number.isNaN(value)) return "—";
    return (value * 100).toFixed(2) + "%";
  }

  function fmtVol(value) {
    if (value == null || Number.isNaN(value)) return "—";
    const abs = Math.abs(value);
    if (abs >= 1e8) return (value / 1e8).toFixed(2) + " 亿";
    if (abs >= 1e4) return (value / 1e4).toFixed(2) + " 万";
    return value.toLocaleString("en-US", { maximumFractionDigits: 2 });
  }

  function priceFormat(denom) {
    return denom === "sky"
      ? { type: "price", precision: 6, minMove: 0.000001 }
      : { type: "price", precision: 2, minMove: 0.01 };
  }

  function candleStats(candle) {
    const denom = lastData.denomination;
    const idx = indexByTime.get(Math.floor(candle.t / 1000));
    const prev = idx > 0 ? lastData.candles[idx - 1] : null;
    const base = prev ? prev.c : candle.o;
    const diff = candle.c - base;
    const chg = base ? diff / base : 0;
    const amp = candle.o ? (candle.h - candle.l) / candle.o : 0;
    const up = diff >= 0;
    return {
      date: fmtTime(candle.t, lastData.interval),
      o: fmtPrice(candle.o, denom),
      h: fmtPrice(candle.h, denom),
      l: fmtPrice(candle.l, denom),
      c: fmtPrice(candle.c, denom),
      diff: (up ? "+" : "-") + fmtPrice(Math.abs(diff), denom),
      chg: (up ? "+" : "-") + fmtPct(Math.abs(chg)),
      amp: fmtPct(amp),
      v: fmtVol(candle.v) + (denom === "sky" ? " SKY" : " MKR"),
      qv: fmtVol(candle.qv) + " USDT",
      src: SRC_LABEL[candle.src] || candle.src,
      up,
    };
  }

  function paint(el, text, up) {
    el.textContent = text;
    el.classList.remove("up", "down");
    if (up === true) el.classList.add("up");
    if (up === false) el.classList.add("down");
  }

  function applyLegend(stats, pinned) {
    legend.date.textContent = stats.date;
    legend.o.textContent = stats.o;
    paint(legend.h, stats.h, true);
    paint(legend.l, stats.l, false);
    paint(legend.c, stats.c, stats.up);
    paint(legend.chg, stats.chg + " (" + stats.diff + ")", stats.up);
    legend.amp.textContent = stats.amp;
    legend.v.textContent = stats.v;
    legend.src.textContent = stats.src;
    pinBadge.classList.toggle("hidden", !pinned);
  }

  function applyTooltip(stats, pinned) {
    tooltipEl.innerHTML =
      `<div class="tt-date">${stats.date}</div>` +
      `<div class="tt-row"><span>来源</span><span>${stats.src}</span></div>` +
      `<div class="tt-row"><span>开</span><span>${stats.o}</span></div>` +
      `<div class="tt-row"><span>高</span><span class="up">${stats.h}</span></div>` +
      `<div class="tt-row"><span>低</span><span class="down">${stats.l}</span></div>` +
      `<div class="tt-row"><span>收</span><span class="${stats.up ? "up" : "down"}">${stats.c}</span></div>` +
      `<div class="tt-row"><span>涨跌</span><span class="${stats.up ? "up" : "down"}">${stats.chg}</span></div>` +
      `<div class="tt-row"><span>涨跌额</span><span class="${stats.up ? "up" : "down"}">${stats.diff}</span></div>` +
      `<div class="tt-row"><span>振幅</span><span>${stats.amp}</span></div>` +
      `<div class="tt-row"><span>成交量</span><span>${stats.v}</span></div>` +
      `<div class="tt-row"><span>成交额</span><span>${stats.qv}</span></div>` +
      `<div class="tt-foot">${pinned ? "已钉住 · 再点空白处或按 Esc 取消" : "点击此 K 线可钉住"}</div>`;
  }

  function placeTooltip(point) {
    if (!point) return;
    const wrap = chartEl.parentElement;
    const w = wrap.clientWidth;
    const h = wrap.clientHeight;
    const tw = tooltipEl.offsetWidth || 220;
    const th = tooltipEl.offsetHeight || 240;
    let left = point.x + 16;
    let top = point.y + 16;
    if (left + tw > w - 8) left = point.x - tw - 16;
    if (top + th > h - 8) top = point.y - th - 16;
    if (left < 8) left = 8;
    if (top < 36) top = 36;
    tooltipEl.style.left = left + "px";
    tooltipEl.style.top = top + "px";
  }

  function showCandle(candle, opts) {
    if (!candle || !lastData) return;
    const pinned = !!(opts && opts.pinned);
    const stats = candleStats(candle);
    applyLegend(stats, pinned);
    applyTooltip(stats, pinned);
    tooltipEl.classList.remove("hidden");
    if (opts && opts.point) placeTooltip(opts.point);
  }

  function hideTooltipIfUnpinned() {
    if (pinnedTime != null) return;
    tooltipEl.classList.add("hidden");
    if (lastData && lastData.candles.length) {
      applyLegend(candleStats(lastData.candles[lastData.candles.length - 1]), false);
    }
  }

  function spliceMarker() {
    if (!lastData) return [];
    return [
      {
        time: Math.floor(lastData.cutover_ms / 1000),
        position: "aboveBar",
        color: "#f0b90b",
        shape: "arrowDown",
        text: "MKR → SKY",
      },
    ];
  }

  function refreshMarkers() {
    if (!candleSeries) return;
    const markers = spliceMarker();
    if (pinnedTime != null) {
      markers.push({
        time: pinnedTime,
        position: "belowBar",
        color: "#f0b90b",
        shape: "circle",
        text: "选中",
      });
    }
    candleSeries.setMarkers(markers);
  }

  function pinAt(timeSec, point) {
    const candle = byTime.get(timeSec);
    if (!candle) return;
    pinnedTime = timeSec;
    showCandle(candle, { pinned: true, point });
    refreshMarkers();
  }

  function unpin() {
    pinnedTime = null;
    refreshMarkers();
    hideTooltipIfUnpinned();
  }

  function ensureChart() {
    if (chart) return;
    chart = LightweightCharts.createChart(chartEl, {
      layout: {
        background: { color: "#0b0e11" },
        textColor: "#848e9c",
      },
      grid: {
        vertLines: { color: "#1e2329" },
        horzLines: { color: "#1e2329" },
      },
      crosshair: {
        mode: LightweightCharts.CrosshairMode.MagnetOHLC ?? LightweightCharts.CrosshairMode.Magnet,
        vertLine: {
          color: "#848e9c",
          width: 1,
          style: LightweightCharts.LineStyle.Dashed,
          labelBackgroundColor: "#2b3139",
        },
        horzLine: {
          color: "#848e9c",
          width: 1,
          style: LightweightCharts.LineStyle.Dashed,
          labelBackgroundColor: "#2b3139",
        },
      },
      rightPriceScale: { borderColor: "#2b3139" },
      timeScale: {
        borderColor: "#2b3139",
        timeVisible: true,
        secondsVisible: false,
      },
      handleScroll: { mouseWheel: true, pressedMouseMove: true, horzTouchDrag: true },
      handleScale: { axisPressedMouseMove: true, mouseWheel: true, pinch: true },
    });
    candleSeries = chart.addCandlestickSeries({
      upColor: "#0ecb81",
      downColor: "#f6465d",
      borderVisible: false,
      wickUpColor: "#0ecb81",
      wickDownColor: "#f6465d",
      priceFormat: priceFormat(denomination),
    });
    volumeSeries = chart.addHistogramSeries({
      priceFormat: { type: "volume" },
      priceScaleId: "vol",
    });
    chart.priceScale("vol").applyOptions({
      scaleMargins: { top: 0.8, bottom: 0 },
    });

    chart.subscribeCrosshairMove((param) => {
      if (!param || param.time == null || !param.point) {
        hideTooltipIfUnpinned();
        return;
      }
      const timeSec = typeof param.time === "number" ? param.time : Date.UTC(param.time.year, param.time.month - 1, param.time.day) / 1000;
      if (pinnedTime != null) return;
      const candle = byTime.get(timeSec);
      if (!candle) {
        hideTooltipIfUnpinned();
        return;
      }
      showCandle(candle, { point: param.point, pinned: false });
    });

    chart.subscribeClick((param) => {
      if (!param || param.time == null) {
        unpin();
        return;
      }
      const timeSec = typeof param.time === "number" ? param.time : Date.UTC(param.time.year, param.time.month - 1, param.time.day) / 1000;
      if (pinnedTime === timeSec) {
        unpin();
        return;
      }
      pinAt(timeSec, param.point);
    });

    window.addEventListener("resize", () => {
      chart.applyOptions({ width: chartEl.clientWidth, height: chartEl.clientHeight });
    });
  }

  function setDenom(next) {
    denomination = next;
    denomButtons.forEach((btn) => {
      btn.classList.toggle("on", btn.dataset.denom === next);
    });
    load();
  }

  async function loadFromBinance(interval) {
    statusEl.textContent = "正在从 Binance 拉取 MKR / SKY 历史 K 线…";
    return window.MkrSkyKline.fetchMerged(interval, denomination, (symbol, n) => {
      statusEl.textContent = "正在拉取 " + symbol + "（已 " + n + " 根）…";
    });
  }

  async function load() {
    ensureChart();
    const interval = intervalEl.value;
    statusEl.textContent = "正在加载 K 线…";
    try {
      let data = null;
      if (location.protocol !== "file:") {
        try {
          const res = await fetch(
            "/api/klines?interval=" +
              encodeURIComponent(interval) +
              "&denomination=" +
              encodeURIComponent(denomination)
          );
          if (res.ok) data = await res.json();
        } catch (_err) {
          data = null;
        }
      }
      if (!data) data = await loadFromBinance(interval);
      render(data);
    } catch (err) {
      statusEl.textContent =
        "加载失败：" +
        err.message +
        "。不要只用 127.0.0.1 打开空白页；请双击 web/index.html，或先在本机运行 python3 -m mkr_sky serve。若 Binance 打不开，需要能访问国际行情的网络。";
    }
  }

  function render(data) {
    const candles = data.candles || [];
    if (!candles.length) {
      statusEl.textContent = "没有 K 线数据。";
      return;
    }

    pinnedTime = null;
    byTime = new Map();
    indexByTime = new Map();
    candles.forEach((c, i) => {
      const t = Math.floor(c.t / 1000);
      byTime.set(t, c);
      indexByTime.set(t, i);
    });

    candleSeries.applyOptions({ priceFormat: priceFormat(data.denomination) });
    candleSeries.setData(
      candles.map((c) => ({
        time: Math.floor(c.t / 1000),
        open: c.o,
        high: c.h,
        low: c.l,
        close: c.c,
      }))
    );
    volumeSeries.setData(
      candles.map((c) => ({
        time: Math.floor(c.t / 1000),
        value: c.v,
        color: c.c >= c.o ? "rgba(14,203,129,0.45)" : "rgba(246,70,93,0.45)",
      }))
    );

    lastData = data;
    refreshMarkers();
    chart.timeScale().fitContent();

    const last = candles[candles.length - 1];
    const prev = candles.length > 1 ? candles[candles.length - 2] : last;
    const change = (last.c - prev.c) / prev.c;
    lastPriceEl.textContent = fmtPrice(last.c, data.denomination) + " " + data.denomination.toUpperCase();
    changeEl.textContent = (change >= 0 ? "+" : "") + (change * 100).toFixed(2) + "%";
    changeEl.className = "v " + (change >= 0 ? "up" : "down");
    coverageEl.textContent =
      fmtTime(candles[0].t, "1d").slice(0, 10) + " → " + fmtTime(last.t, "1d").slice(0, 10);
    cutoverEl.textContent = fmtTime(data.cutover_ms, data.interval);
    spliceErrEl.textContent =
      data.splice && data.splice.rel_error != null
        ? (data.splice.rel_error * 100).toFixed(4) + "%"
        : "—";
    sourcesEl.textContent = `MKR ${data.mkr_bars} 根 / SKY ${data.sky_bars} 根 / 合并 ${data.merged_bars} 根`;
    applyLegend(candleStats(last), false);
    tooltipEl.classList.add("hidden");
    statusEl.textContent = "移动鼠标查看每根 K 线的开高低收；点击可钉住，Esc 或点空白处取消。滚轮缩放，拖动平移。";
  }

  denomButtons.forEach((btn) => {
    btn.addEventListener("click", () => setDenom(btn.dataset.denom));
  });
  intervalEl.addEventListener("change", load);
  zoomBtn.addEventListener("click", () => {
    if (!chart || !lastData || !lastData.candles.length) return;
    const candles = lastData.candles;
    const cut = lastData.cutover_ms;
    let idx = candles.findIndex((c) => c.t >= cut);
    if (idx < 0) idx = candles.length - 1;
    const from = candles[Math.max(0, idx - 90)];
    const to = candles[Math.min(candles.length - 1, idx + 40)];
    chart.timeScale().setVisibleRange({
      from: Math.floor(from.t / 1000),
      to: Math.floor(to.t / 1000),
    });
  });

  document.addEventListener("keydown", (ev) => {
    if (!lastData) return;
    if (ev.key === "Escape") {
      unpin();
      return;
    }
    if (pinnedTime == null) return;
    const idx = indexByTime.get(pinnedTime);
    if (idx == null) return;
    if (ev.key === "ArrowLeft" && idx > 0) {
      ev.preventDefault();
      pinAt(Math.floor(lastData.candles[idx - 1].t / 1000));
    } else if (ev.key === "ArrowRight" && idx < lastData.candles.length - 1) {
      ev.preventDefault();
      pinAt(Math.floor(lastData.candles[idx + 1].t / 1000));
    }
  });

  load();
})();
