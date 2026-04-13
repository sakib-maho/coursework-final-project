"""HTML parsing helpers for rental listings."""

from html.parser import HTMLParser


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if href and href.startswith(("http://", "https://", "/")):
            self.links.append(href)


def extract_links(html: str) -> list[str]:
    collector = LinkCollector()
    collector.feed(html)
    return collector.links
