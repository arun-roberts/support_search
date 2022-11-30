import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array):
    # Making a GET request
    r = requests.get('https://www.memomusichall.com.au/')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.select("div.gig-inner")

    del s[2]

    for each in s:
        gig = { 
            "title": each.select_one("div.gig-band-name a").string,
            "description": each.select_one('div.gig-excerpt p').string,
            "artists": [each.select('h2.text-center a')[0].string],
            "venue": "Memo Music Hall, St Kilda",
            "when": "",
            "link": each.select('h2.text-center a')[0]['href'],
            "genre": ""
        }
        gig_supports = each.select('h4.gig-support-band-name')
        if (len(gig_supports) != 0):
            gig["artists"].append(gig_supports[0].string)
        gig_date = each.select('div.gig-doors-open h2')[0].string.split()
        gig_date.pop()
        if (int(gig_date[1]) < 10):
            padded = '0' + gig_date[1]
            gig_date[1] = padded
        if (len(gig_date[3]) == 6):
            pad_it = '0' + gig_date[3]
            gig_date[3] = pad_it
        gig["when"] = str(datetime.strptime(' '.join(gig_date), '%a %d %b, %I:%M%p'))
        gigs_array.append(gig)
