from dataclasses import dataclass


@dataclass(frozen=True)
class FeedSource:
    name: str
    url: str


FEED_SOURCES = [
    FeedSource(name="No Film School", url="https://nofilmschool.com/rss.xml"),
    FeedSource(name="Film Riot", url="https://www.filmriot.com/feed/"),
    FeedSource(name="IndieWire Film", url="https://www.indiewire.com/c/film/feed/"),
    FeedSource(name="RedShark News", url="https://www.redsharknews.com/rss.xml"),
]

MAX_ITEMS_PER_FEED = 5
SUMMARY_SENTENCES = 3
