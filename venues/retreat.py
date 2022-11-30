import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://retreathotelbrunswick.squarespace.com/music')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.select("div.summary-item-record-type-event")

    today = datetime.now()
    
    for each in s:
        gig = { 
            "title": each.find(class_="summary-title-link").string,
            "description": "",
            "artists": [],
            "venue": "The Retreat, Brunswick",
            "when": "",
            "link": 'https://retreathotelbrunswick.squarespace.com' + each.find(class_='summary-title-link')['href'],
            "genre": ""
        }
        gig_date = each.find(class_='summary-thumbnail-event-date-day').string
        if (int(gig_date) < 10):
            gig_date = "0" + gig_date
        gig_month = each.find(class_='summary-thumbnail-event-date-month').string
        when_string = gig_date + ' ' + gig_month
        year_string = "2022"
        if (today.month > datetime.strptime(gig_month, '%b').month):
            year_string = str(today.year + 1)
        gig["when"] = str(datetime.strptime(year_string + " " + when_string, '%Y %d %b'))
        gigs_array.append(gig)