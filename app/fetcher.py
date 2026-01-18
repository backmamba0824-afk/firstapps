from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from typing import Iterable

import feedparser
import requests
from bs4 import BeautifulSoup

from .config import FEED_SOURCES, MAX_ITEMS_PER_FEED


@dataclass(frozen=True)
class Article:
    title: str
    url: str
    source: str
    published: dt.datetime | None
    summary: str
    content: str


def _parse_date(entry: feedparser.FeedParserDict) -> dt.datetime | None:
    if "published_parsed" in entry and entry.published_parsed:
        return dt.datetime(*entry.published_parsed[:6], tzinfo=dt.timezone.utc)
    return None


def _fetch_article_text(url: str) -> str:
    response = requests.get(url, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav"]):
        tag.decompose()
    text = " ".join(chunk.strip() for chunk in soup.stripped_strings)
    return text


def fetch_articles() -> list[Article]:
    articles: list[Article] = []
    for source in FEED_SOURCES:
        feed = feedparser.parse(source.url)
        for entry in feed.entries[:MAX_ITEMS_PER_FEED]:
            url = entry.get("link", "")
            if not url:
                continue
            summary = entry.get("summary", "")
            try:
                content = _fetch_article_text(url)
            except requests.RequestException:
                content = summary
            articles.append(
                Article(
                    title=entry.get("title", "(untitled)"),
                    url=url,
                    source=source.name,
                    published=_parse_date(entry),
                    summary=summary,
                    content=content,
                )
            )
    return articles


def sort_articles(articles: Iterable[Article]) -> list[Article]:
    return sorted(
        articles,
        key=lambda article: article.published or dt.datetime.min.replace(tzinfo=dt.timezone.utc),
        reverse=True,
    )
