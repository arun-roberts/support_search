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
            "link": each.select('h2.text-center a')['href'],
            "sold_out": "",
            "genre": ""
        }
        gig_date = each.select('gig-doors-open h2')[0].string.split()
        gig_date.pop()
        if (abs(gig_date[1]) < 10):
            padded = '0' + gig_date[1]
            gig_date[1] = padded
        if (len(gig_date[3]) == 6):
            pad_it = '0' + gig_date[3]
            gig_date[3] = pad_it
        gig["when"] = str(datetime.strptime(' '.join(gig_date), '%a %d %b, %I:%M%p'))
        gigs_array.append(gig)

    gig_scraper([])