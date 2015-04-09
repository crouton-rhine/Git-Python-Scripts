import feedparser

python_wiki_rss_url = "http://www.tvrage.com/myweekrss.php"

feeds = feedparser.parse(python_wiki_rss_url)
attrs = []
for i in feeds:
	attrs.append(i)
print(attrs)
print(len(feeds.entries))
print(feeds.entries[792])

num = 0
while num < len(feeds.entries):
	print(feeds.entries[num].title)
	num += 1
	#if i == "entries":
	#	print(getattr(feeds, i)[15].title)
	#if i != "entries":
	#	print(feeds[i])


