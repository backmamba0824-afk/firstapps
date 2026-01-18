from __future__ import annotations

import argparse
from pathlib import Path

from .fetcher import fetch_articles, sort_articles
from .report import build_report, render_markdown


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="映像制作ニュースのデイリーまとめを生成します。")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("daily_report.md"),
        help="生成するMarkdownレポートの出力先",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="レポートに含める記事数",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    articles = sort_articles(fetch_articles())
    report = build_report(articles[: args.limit])
    content = render_markdown(report)
    args.output.write_text(content, encoding="utf-8")
    print(f"Wrote report to {args.output}")


if __name__ == "__main__":
    main()
