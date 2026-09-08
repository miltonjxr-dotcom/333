(() => {
  const RATIO = 24000;
  const BINANCE_URLS = [
    "https://data-api.binance.vision/api/v3/klines",
    "https://api.binance.com/api/v3/klines",
  ];

  function toCandle(row, src) {
    return {
      t: Number(row[0]),
      o: Number(row[1]),
      h: Number(row[2]),
      l: Number(row[3]),
      c: Number(row[4]),
      v: Number(row[5]),
      ct: Number(row[6]),
      qv: Number(row[7]),
      src,
    };
  }

  function convertMkr(bar, denom) {
    if (denom === "mkr") return Object.assign({}, bar, { src: "mkr" });
    return Object.assign({}, bar, {
      o: bar.o / RATIO,
      h: bar.h / RATIO,
      l: bar.l / RATIO,
      c: bar.c / RATIO,
      v: bar.v * RATIO,
      src: "mkr",
    });
  }

  function convertSky(bar, denom) {
    if (denom === "sky") return Object.assign({}, bar, { src: "sky" });
    return Object.assign({}, bar, {
      o: bar.o * RATIO,
      h: bar.h * RATIO,
      l: bar.l * RATIO,
      c: bar.c * RATIO,
      v: bar.v / RATIO,
      src: "sky",
    });
  }

  function spliceOverlap(mkrBar, skyBar) {
    return {
      t: mkrBar.t,
      o: mkrBar.o,
      h: Math.max(mkrBar.h, skyBar.h),
      l: Math.min(mkrBar.l, skyBar.l),
      c: skyBar.c,
      v: mkrBar.v + skyBar.v,
      qv: mkrBar.qv + skyBar.qv,
      ct: Math.max(mkrBar.ct, skyBar.ct),
      src: "splice",
    };
  }

  function mergeKlines(mkr, sky, denomination) {
    const byTime = new Map();
    mkr.forEach((bar) => byTime.set(bar.t, convertMkr(bar, denomination)));
    sky.forEach((bar) => {
      const converted = convertSky(bar, denomination);
      const existing = byTime.get(bar.t);
      byTime.set(bar.t, existing ? spliceOverlap(existing, converted) : converted);
    });
    return Array.from(byTime.values()).sort((a, b) => a.t - b.t);
  }

  function spliceQuality(mkr, sky) {
    if (!mkr.length || !sky.length) {
      return { rel_error: null, abs_error: null, last_mkr_close: null, first_sky_open: null };
    }
    const lastMkr = mkr[mkr.length - 1];
    const firstSky = sky[0];
    const mkrAsSky = lastMkr.c / RATIO;
    const absError = Math.abs(mkrAsSky - firstSky.o);
    return {
      last_mkr_close: lastMkr.c,
      first_sky_open: firstSky.o,
      mkr_as_sky: mkrAsSky,
      abs_error: absError,
      rel_error: firstSky.o ? absError / firstSky.o : null,
      last_mkr_open_time: lastMkr.t,
      first_sky_open_time: firstSky.t,
    };
  }

  async function fetchJson(url) {
    const res = await fetch(url);
    if (!res.ok) throw new Error("HTTP " + res.status);
    return res.json();
  }

  async function fetchBinanceKlines(symbol, interval, src, onProgress) {
    let lastError = null;
    for (const base of BINANCE_URLS) {
      try {
        const out = [];
        let startTime = 0;
        for (;;) {
          const url =
            base +
            "?symbol=" +
            encodeURIComponent(symbol) +
            "&interval=" +
            encodeURIComponent(interval) +
            "&limit=1000&startTime=" +
            startTime;
          const raw = await fetchJson(url);
          if (!Array.isArray(raw) || raw.length === 0) break;
          raw.forEach((row) => out.push(toCandle(row, src)));
          if (onProgress) onProgress(symbol, out.length);
          if (raw.length < 1000) break;
          startTime = Number(raw[raw.length - 1][0]) + 1;
        }
        if (out.length) return out;
      } catch (err) {
        lastError = err;
      }
    }
    throw lastError || new Error("无法拉取 " + symbol);
  }

  async function fetchMerged(interval, denomination, onProgress) {
    const [mkr, sky] = await Promise.all([
      fetchBinanceKlines("MKRUSDT", interval, "mkr", onProgress),
      fetchBinanceKlines("SKYUSDT", interval, "sky", onProgress),
    ]);
    const candles = mergeKlines(mkr, sky, denomination);
    return {
      ratio: RATIO,
      interval,
      denomination,
      cutover_ms: sky.length ? sky[0].t : 1758067200000,
      mkr_bars: mkr.length,
      sky_bars: sky.length,
      merged_bars: candles.length,
      splice: spliceQuality(mkr, sky),
      candles,
    };
  }

  window.MkrSkyKline = { RATIO, mergeKlines, fetchMerged, spliceQuality };
})();
