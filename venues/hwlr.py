import requests
import json
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.moshtix.com.au/mosh2/rss/GenerateFeed.aspx?feedCode=636851343092690293')
 
# Parsing the XML
soup = BeautifulSoup(r.content, 'xml')
 
s = soup.find_all('item')
 
gigs = []

for each in s:
    obj = { 
        "title": each.title.string,
        "description": each.description.string,
        "artists": [],
        "venue": each.find('moshtix:venuetitle').string,
        "when": each.find('moshtix:eventstartdatetime').string,
        "link": each.link.string,
        "sold_out": each.find('moshtix:soldout').string,
        "genre": each.genre.string
    }
    for artist in each.find('moshtix:artists'):
        str = artist.string
        if (str != "howler" and str != "hwlr" and str != "\n"):
            obj["artists"].append(str)
    gigs.append(obj)

with open("hwlr_test.js", "w") as j:
    json.dump(gigs, j)  

