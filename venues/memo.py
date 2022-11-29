import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def gig_scraper(gigs_array):
    # Making a GET request
    r = requests.get('https://www.memomusichall.com.au/')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.select("div.gig-inner")
    print(s)
    
    for each in s:
        gig = { 
            "title": each.select("h2.text-center a")[0].string,
            "description": each.select('div.gig-excerpt p')[0].string,
            "artists": [each.select('h2.text-center a')[0].string, each.select('h4.gig-support-band-name')[0].string],
            "venue": "Memo Music Hall, St Kilda",
            "when": "",
            "link": 'https://retreathotelbrunswick.squarespace.com' + each.find(class_='summary-title-link')['href'],
            "sold_out": "",
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

    gig_scraper([])