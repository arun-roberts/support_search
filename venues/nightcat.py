import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://www.thenightcat.com.au/shows')
    
    # Parsing the XML
    soup = BeautifulSoup(r.content, 'html')
    
    s = soup.select('gig-individual-wrapper')

    today = datetime.now()
    
    for each in s:
        gig = { 
            "title": each.find(class_="gig-title").string,
            "description": "",
            "artists": [],
            "venue": "The Nightcat",
            "when": "",
            "link": each.find(class_="gig-title")["href"].string,
            "genre": ""
        }
        supports = each.find(class_="gig-guests").string
        if (supports != None and len(supports) > 0):
            gig["artists"].append(supports)
        when_string = each.find(class_='gig-date').string
        gig["when"] = str(datetime.strptime(when_string, '%A %d %B %Y'))
        gigs_array.append(gig)
        print(gig)
        
scrape_it([])
