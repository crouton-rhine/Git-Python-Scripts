import feedparser
import bisect

tv_shows_url = "http://www.tvrage.com/myweekrss.php"
feeds = feedparser.parse(tv_shows_url)

tvshows = ["Arrow", "Flash", "Blacklist", "Nine-Nine", "Suits"]

#allows me to make keyword database for my shows
num = 0
title_list = []
while num < len(feeds.entries):
	title_list.append((feeds.entries[num].title).split())
	num += 1

#creates list of "code numbers" for my shows that ARE on this week
titleno = 0
show_codes = []
while titleno < len(feeds.entries):
	for show in tvshows:
		if show in title_list[titleno]:
			show_codes.append(titleno)
	titleno += 1

#creates list of dates
number = 0
key_list = []
while number < len(feeds.entries):
	if feeds.entries[number].link == "http://www.tvrage.com":
		key_list.append(number)
	number += 1

#function below copied from bisect documentation
def find_le(a, x):
    #'Find rightmost value less than or equal to x'
    i = bisect.bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

for code in show_codes:
	print(feeds.entries[find_le(key_list, code)].title)
	print(feeds.entries[code].title)

#print(feeds.entries[411].title)
#print(key_list)
#print(title_list[463])
#print(show_codes)
