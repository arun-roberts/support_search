import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://www.eventbrite.com.au/org/29979026424/showmore/?page_size=24&type=future&page=1')
    
    # Parsing the XML
    soup = BeautifulSoup(r.content, 'html')
    
    s = soup.select('eventLink all bandroom')

    today = datetime.now()
    
    for each in s:
        gig = { 
            "title": r.,
            "description": "",
            "artists": [],
            "venue": "170 Russell",
            "when": "",
            "link": each["href"].string,
            "genre": ""
        }
        supports = each.find(class_="support")
        if (supports != None):
            gig["artists"].append(supports.string)
        when_arr = ' '.split(each.find(class_='date').string)
        year_string = "2022"
        if (today.month > datetime.strptime(when_arr[2], '%b').month):
            year_string = str(today.year + 1)
        gig["when"] = str(datetime.strptime(when_arr.join(' ') + ' ' + year_string, '%a %d %b %Y'))
        when_string = each.find(class_='gig-date').string
        gig["when"] = str(datetime.strptime(when_string, '%A %d %B %Y'))
        gigs_array.append(gig)
        print(gig)
        
scrape_it([])

