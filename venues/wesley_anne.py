import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

# Making a GET request
r = requests.get('https://wesleyanne.com.au/events')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')


s = soup.select("article.eventlist-event")
 
gigs = []

for each in s:
    gig = { 
        "title": each.find(class_="eventlist-title-link").string,
        "description": "",
        "artists": [],
        "venue": "The Retreat, Brunswick",
        "when": "",
        "link": 'https://wesleyanne.com.au' + each.find(class_='eventlist-title-link')['href'],
        "sold_out": "",
        "genre": ""
    }
    for p in each.find_all(attrs={"style": "white-space:pre-wrap;"}):
        st = p.string
        if (st == None):
            st = "\n"
        holder = gig["description"]
        gig["description"] = holder + st
    when_string = each.find(class_='event-date').string + ' ' + each.find(class_="event-time-24hr-start").string
    gig["when"] = datetime.strptime(when_string, '%A, %d %B %Y %H:%M')
    gigs.append(gig)

print(gigs)
