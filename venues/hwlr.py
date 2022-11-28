import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://www.moshtix.com.au/mosh2/rss/GenerateFeed.aspx?feedCode=636851343092690293')
    
    # Parsing the XML
    soup = BeautifulSoup(r.content, 'xml')
    
    s = soup.find_all('item')
    
    for each in s:
        gig = { 
            "title": each.title.string,
            "description": each.description.string,
            "artists": [],
            "venue": each.find('moshtix:venuetitle').string,
            "when": "",
            "link": each.link.string,
            "sold_out": each.find('moshtix:soldout').string,
            "genre": each.genre.string
        }
        when_string = each.find('moshtix:eventstartdatetime').string
        gig["when"] = str(datetime.strptime(when_string, '%a, %d %b %Y %H:%M'))
        for artist in each.find('moshtix:artists'):
            art = artist.string
            if (str != "howler" and str != "hwlr" and str != "\n"):
                gig["artists"].append(art)
        gigs_array.append(gig)
