import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://170russell.com/upcoming-events/')
    
    # Parsing the XML
    soup = BeautifulSoup(r.content, 'html')
    
    s = soup.select('gig-infos')
    
    for each in s:
        gig = { 
            "title": each.find(class_="gig-title").string,
            "description": each.find(class_="gig-quests").string,
            "artists": [],
            "venue": "170 Russell",
            "when": "",
            "link": each.find(class_="gig-title")["href"].string,
            "genre": each.genre.string
        }
        when_string = each.find(class_='gig-date').string
        gig["when"] = str(datetime.strptime(when_string, '%A %d %B %Y'))
        gigs_array.append(gig)
        print(gig)
        
scrape_it([])
