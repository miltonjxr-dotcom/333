# MKR × SKY 合并 K 线

Maker 换成 Sky 之后，SKY 自己的 K 线太短，直接看参考价值偏低。这个工具把 **Binance `MKRUSDT` 历史 K 线** 和 **`SKYUSDT` 实盘 K 线** 接成一条连续序列。

换算用协议固定比例：

**1 MKR = 24,000 SKY**

（延迟升级罚金只影响链上兑换到账数量，不影响价格口径，图表始终用 24,000。）

## 拼接规则

| 段 | 数据 | 时间（Binance） |
| --- | --- | --- |
| 历史 | `MKRUSDT` | 约 2020-07-23 → 2025-09-15 02:00 UTC（随后停牌摘牌） |
| 当前 | `SKYUSDT` | 2025-09-17 08:00 UTC 起 |

- **以 SKY 为准**：MKR 的 OHLC ÷ 24,000，MKR 成交量 × 24,000。
- **以 MKR 为准**：SKY 的 OHLC × 24,000，SKY 成交量 ÷ 24,000。
- 同一根 K 线两边都有（周线 / 月线常见）：开盘用 MKR，收盘用 SKY，最高/最低取两端极值，成交量相加。

日线上，末根 MKR 收盘 `1813.7` ÷ 24,000 ≈ `0.0755708`，与 SKY 首根开盘 `0.07558` 几乎贴齐。

## 怎么打开（在你自己的电脑上）

之前说的 `http://127.0.0.1:8000` 是**你这台电脑**上的地址。云端起的服务到不了你的 Chrome，所以会提示「拒绝了连接请求」。

最简单：下载本分支压缩包，解压后**双击** `web/index.html`（图表会直接向 Binance 拉 K 线，不用先起服务器）。

https://github.com/miltonjxr-dotcom/333/archive/refs/heads/cursor/mkr-sky-kline-merge-cc83.zip

或者在本机终端运行：

```bash
python3 -m pip install -r requirements.txt
python3 -m mkr_sky serve --host 127.0.0.1 --port 8000
```

Windows 也可以双击 `run.bat`。页面上可以切换日/周/小时周期、SKY / MKR 口径，以及**线性 / 对数**坐标。鼠标在图上移动或点击某一根 K 线，会显示该根的开、高、低、收、涨跌、振幅和成交量；点击可钉住，Esc 取消。

导出 CSV / JSON：

```bash
python3 -m mkr_sky export --interval 1d --denomination sky -o sky_merged.csv
python3 -m mkr_sky export --interval 1d --denomination mkr --format json -o mkr_merged.json
```

数据走 Binance 公开行情镜像 `data-api.binance.vision`（无需 API key），历史 K 线会缓存在 `.cache/klines/`。

## 测试

```bash
python3 -m pytest -q
```
