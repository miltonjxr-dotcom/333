from mkr_sky.cli import build_parser


def test_parser_export_defaults():
    args = build_parser().parse_args(["export", "-o", "out.csv"])
    assert args.interval == "1d"
    assert args.denomination == "sky"
    assert args.format == "csv"


def test_parser_serve_port():
    args = build_parser().parse_args(["serve", "--port", "9001"])
    assert args.port == 9001
