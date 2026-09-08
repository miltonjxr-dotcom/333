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
  const denomButtons = document.querySelectorAll("[data-denom]");

  let denomination = "sky";
  let chart;
  let candleSeries;
  let volumeSeries;

  function fmtTime(ms) {
    return new Date(ms).toISOString().slice(0, 16).replace("T", " ") + " UTC";
  }

  function fmtPrice(value, denom) {
    if (value == null || Number.isNaN(value)) return "—";
    if (denom === "sky") return value.toFixed(6);
    return value.toLocaleString("en-US", { maximumFractionDigits: 2 });
  }

  function fmtPct(value) {
    if (value == null) return "—";
    const pct = (value * 100).toFixed(4);
    return pct + "%";
  }

  function priceFormat(denom) {
    return denom === "sky"
      ? { type: "price", precision: 6, minMove: 0.000001 }
      : { type: "price", precision: 2, minMove: 0.01 };
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
      crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
      rightPriceScale: { borderColor: "#2b3139" },
      timeScale: { borderColor: "#2b3139", timeVisible: true },
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

  async function load() {
    ensureChart();
    const interval = intervalEl.value;
    statusEl.textContent = "正在拉取并合并 K 线…";
    try {
      const res = await fetch(
        `/api/klines?interval=${encodeURIComponent(interval)}&denomination=${encodeURIComponent(denomination)}`
      );
      if (!res.ok) {
        throw new Error(await res.text());
      }
      const data = await res.json();
      render(data);
    } catch (err) {
      statusEl.textContent = "加载失败：" + err.message;
    }
  }

  function render(data) {
    const candles = data.candles || [];
    if (!candles.length) {
      statusEl.textContent = "没有 K 线数据。";
      return;
    }

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

    const cutoverSec = Math.floor(data.cutover_ms / 1000);
    candleSeries.setMarkers([
      {
        time: cutoverSec,
        position: "aboveBar",
        color: "#f0b90b",
        shape: "arrowDown",
        text: "MKR → SKY",
      },
    ]);
    chart.timeScale().fitContent();

    const last = candles[candles.length - 1];
    const prev = candles.length > 1 ? candles[candles.length - 2] : last;
    const change = (last.c - prev.c) / prev.c;
    lastPriceEl.textContent = fmtPrice(last.c, data.denomination) + " " + data.denomination.toUpperCase();
    changeEl.textContent = (change >= 0 ? "+" : "") + (change * 100).toFixed(2) + "%";
    changeEl.className = "v " + (change >= 0 ? "up" : "down");
    coverageEl.textContent =
      fmtTime(candles[0].t).slice(0, 10) + " → " + fmtTime(last.t).slice(0, 10);
    cutoverEl.textContent = fmtTime(data.cutover_ms);
    spliceErrEl.textContent = fmtPct(data.splice && data.splice.rel_error);
    sourcesEl.textContent = `MKR ${data.mkr_bars} 根 / SKY ${data.sky_bars} 根 / 合并 ${data.merged_bars} 根`;
    statusEl.textContent =
      data.denomination === "sky"
        ? "当前按 SKY 计价：历史 MKR 价格 ÷ 24,000，成交量 × 24,000。"
        : "当前按 MKR 计价：SKY 价格 × 24,000，成交量 ÷ 24,000。";
  }

  denomButtons.forEach((btn) => {
    btn.addEventListener("click", () => setDenom(btn.dataset.denom));
  });
  intervalEl.addEventListener("change", load);
  load();
})();
