import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array): 
    # Making a GET request
    r = requests.get('https://www.johncurtinhotel.com/gigs')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.select('div[role="listitem"]')
    
    today = datetime.now()

    for each in s:
        gig = { 
            "title": each.find(class_="heading-4"),
            "description": "",
            "artists": [each.find(class_="heading-4")],
            "venue": "The Curtin, Carlton",
            "when": "",
            "link": each.select('a[href]')[0]['href'],
            "genre": ""
        }
        supports = each.find(class_="heading-5")
        if (supports != None):
            gig["artists"].append(supports.string)
        when_arr = ' '.split(each.find(class_='date').string)
        when_string = when_arr[0] + ' ' + when_arr[1] + ' ' + when_arr[2]
        year_string = "2022"
        if (today.month > datetime.strptime(when_arr[2], '%B').month):
            year_string = str(today.year + 1)
        gig["when"] = str(datetime.strptime(when_string + ' ' + year_string, '%A, %d %B %Y'))
        gigs_array.append(gig)
    print(gigs_array)

scrape_it([])

