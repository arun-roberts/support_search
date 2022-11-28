import requests
import json
from bs4 import BeautifulSoup

def gig_scraper(gigs_array):
    # Making a GET request
    r = requests.get('https://retreathotelbrunswick.squarespace.com/music')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')


    s = soup.select("div.summary-item-record-type-event")
    
    gigs = []

    for each in s:
        gig = { 
            "title": each.find(class_="summary-title-link").string,
            "description": "",
            "artists": [],
            "venue": "The Retreat, Brunswick",
            "when": each.find(class_='summary-thumbnail-event-date-day').string + '' + each.find(class_='summary-thumbnail-event-date-month').string,
            "link": 'https://retreathotelbrunswick.squarespace.com' + each.find(class_='summary-title-link')['href'],
            "sold_out": "",
            "genre": ""
        }
        title = each.find(class_="JSRenderEventTitle").string
        supports = each.find(class_="JSRenderSpecialGuests").string or ""
        gig["artists"].append(title)
        gig["artists"].append(supports)
        gigs.append(gig)
        gigs_array.append(gig)
    return gigs

print(gig_scraper([]))