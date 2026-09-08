from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from mkr_sky.constants import DENOMINATIONS, RATIO, SUPPORTED_INTERVALS
from mkr_sky.fetch import fetch_mkr_and_sky
from mkr_sky.merge import merge_klines, splice_quality


def _export(args: argparse.Namespace) -> int:
    mkr, sky = fetch_mkr_and_sky(args.interval)
    candles = merge_klines(mkr, sky, denomination=args.denomination)
    quality = splice_quality(mkr, sky)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.format == "json":
        payload = {
            "ratio": RATIO,
            "interval": args.interval,
            "denomination": args.denomination,
            "splice": quality,
            "candles": [c.to_api() for c in candles],
        }
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        with out.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(
                fh,
                fieldnames=[
                    "open_time",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume",
                    "quote_volume",
                    "close_time",
                    "source",
                ],
            )
            writer.writeheader()
            for candle in candles:
                writer.writerow(candle.to_csv_row())
    print(
        f"wrote {len(candles)} candles to {out} "
        f"(mkr={len(mkr)} sky={len(sky)} denom={args.denomination})",
        file=sys.stderr,
    )
    return 0


def _serve(args: argparse.Namespace) -> int:
    import uvicorn

    from mkr_sky.server import app

    uvicorn.run(app, host=args.host, port=args.port, log_level="info")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="mkr_sky",
        description="Merge Maker (MKR) and Sky (SKY) klines at 1 MKR = 24,000 SKY.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    export = sub.add_parser("export", help="Write merged OHLCV to CSV or JSON")
    export.add_argument("--interval", choices=SUPPORTED_INTERVALS, default="1d")
    export.add_argument("--denomination", choices=DENOMINATIONS, default="sky")
    export.add_argument("--format", choices=("csv", "json"), default="csv")
    export.add_argument("-o", "--output", required=True)
    export.set_defaults(func=_export)

    serve = sub.add_parser("serve", help="Open the candlestick chart UI")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)
    serve.set_defaults(func=_serve)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
