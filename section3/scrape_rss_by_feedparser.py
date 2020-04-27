import feedparser

d = feedparser.parse('it.rss')

for entry in d.entries:
  print(entry.link, entry.title)