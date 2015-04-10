import feedparser

tv_shows_url = "http://www.tvrage.com/myrss.php"
feeds = feedparser.parse(tv_shows_url)

tvshows = ["Arrow", "Flash", "Blacklist", "Nine-Nine"]

num = 0
title_list = []
while num < len(feeds.entries):
	title_list.append((feeds.entries[num].title).split())
	num += 1

titleno = 0
while titleno < len(feeds.entries):
	for show in tvshows:
		if show in title_list[titleno]:
			print(show + " is on tonight!")
	titleno += 1
