import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('http://affiliateapi.oztix.com.au/v1.9/JSRender.aspx?outlet_id=1495')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find_all("div", class_='JSRenderContainer')

    for each in s:
        gig = { 
            "title": each.find(class_="JSRenderEventTitle").string,
            "description": "",
            "artists": [],
            "venue": each.find(class_="JSRenderVenueName").string,
            "when": "",
            "link": 'https:' + each.find(class_='JSRenderEventTitle')['href'],
            "genre": ""
        }
        title = each.find(class_="JSRenderEventTitle").string
        supports = each.find(class_="JSRenderSpecialGuests").string or ""
        gig["artists"].append(title)
        gig["artists"].append(supports)
        when_string = each.find(class_='JSRenderDate').string
        gig["when"] = str(datetime.strptime(when_string, '%A, %d %B %Y'))
        gigs_array.append(gig)


