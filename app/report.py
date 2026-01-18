from __future__ import annotations

import datetime as dt
from dataclasses import dataclass

from .config import SUMMARY_SENTENCES
from .fetcher import Article
from .summarizer import summarize


@dataclass(frozen=True)
class ReportItem:
    title: str
    url: str
    source: str
    published: str
    summary: list[str]


@dataclass(frozen=True)
class DailyReport:
    date: str
    items: list[ReportItem]


def build_report(articles: list[Article]) -> DailyReport:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    items = []
    for article in articles:
        summary_sentences = summarize(article.content or article.summary, SUMMARY_SENTENCES)
        published = article.published.isoformat() if article.published else "unknown"
        items.append(
            ReportItem(
                title=article.title,
                url=article.url,
                source=article.source,
                published=published,
                summary=summary_sentences,
            )
        )
    return DailyReport(date=today, items=items)


def render_markdown(report: DailyReport) -> str:
    lines = [f"# 映像制作ニュースまとめ ({report.date})", ""]
    for item in report.items:
        lines.append(f"## {item.title}")
        lines.append(f"- Source: {item.source}")
        lines.append(f"- Published: {item.published}")
        lines.append(f"- URL: {item.url}")
        if item.summary:
            lines.append("- Summary:")
            for sentence in item.summary:
                lines.append(f"  - {sentence}")
        else:
            lines.append("- Summary: (要約対象の本文が取得できませんでした)")
        lines.append("")
    return "\n".join(lines).strip() + "\n"
