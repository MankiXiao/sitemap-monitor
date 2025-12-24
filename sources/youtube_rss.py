# sources/youtube_rss.py
import urllib.parse
import feedparser

def youtube_search_feed_url(query: str) -> str:
    # YouTube 搜索 RSS（公开）
    q = urllib.parse.quote_plus(query)
    return f"https://www.youtube.com/feeds/videos.xml?search_query={q}"

def fetch_youtube_items(queries, max_items=30):
    items = []
    for q in queries:
        feed = feedparser.parse(youtube_search_feed_url(q))
        for e in feed.entries[:max_items]:
            items.append({
                "source": "youtube",
                "query": q,
                "title": getattr(e, "title", "") or "",
                "link": getattr(e, "link", "") or "",
                "published": getattr(e, "published", "") or ""
            })
    return items
