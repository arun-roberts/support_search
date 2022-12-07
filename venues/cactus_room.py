import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_it(gigs_array): 
    # Making a GET request
    r = requests.get('http://cactusroom.com.au/events.html')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')

    titles = soup.select('div.event-text h4')
    info = soup.select('div.row div.col-lg.text-center')
    
    today = datetime.now()

    for each in info:
        gig = { 
            "artists": [],
            "venue": "The Cactus Room",
            "when": "",
            "link": each.select('a[href]')[0]['href'],
            "genre": ""
        }
        bands = " / ".split(each.find("h4").string)
        if (len(bands) > 0):
            gig["artists"] = bands
        when_arr = ' '.split(each.find("h5").string)
        if (len(when_arr[1]) < 2):
            padded = "0" + when_arr[1]
            when_arr[1] = padded
        if (len(when_arr[3] > 7)):
            pad_it = "0" + when_arr[3]
            when_arr[3] = pad_it
        year_string = "2022"
        if (today.month > datetime.strptime(when_arr[2], '%B').month):
            year_string = str(today.year + 1)
        gig["when"] = str(datetime.strptime(' '.join(when_arr) + ' ' + year_string, '%b %d - %I:%M%p %Y'))
        gigs_array.append(gig)

    for i, each in titles:
        gigs_array[i]["title"] = each.string
    print(gigs_array)

scrape_it([])

