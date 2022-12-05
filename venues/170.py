import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get("https://moshtix.com.au/mosh2/rss/GenerateFeed.aspx?feedCode=636021192241074672")
    
    # Parsing the XML
    soup = BeautifulSoup(r.content, "xml")

    s = soup.find_all("item")
    
    for each in s:
        gig = { 
            "title": each.title.string,
            "description": each.description.string,
            "artists": [],
            "venue": each.find('moshtix:venuetitle').string,
            "when": "",
            "link": each.link.string,
            "genre": each.genre.string
        }
        when_string = each.find('moshtix:eventstartdatetime').string
        gig["when"] = str(datetime.strptime(when_string, '%a, %d %b %Y %H:%M'))
        for artist in each.find('moshtix:artists'):
            art = artist.string
            if (art != "howler" and art != "hwlr" and art != "\n"):
                gig["artists"].append(art)
        print(gig)

scrape_it([])
