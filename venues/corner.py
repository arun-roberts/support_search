import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

def scrape_it(gigs_array): 
    # Making a GET request
    r = requests.post('https://icgfyqwgtd-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.27.1%3Binstantsearch.js%201.12.1%3BJS%20Helper%202.26.0&x-algolia-application-id=ICGFYQWGTD&x-algolia-api-key=658602a6eeedca93a2ea1125e532f96f', data={"requests":[{"indexName":"prod_cornerhotel_eventguide","params":"query=&hitsPerPage=80&page=0&filters=IsCancelled%20%3A%20false%20AND%20IsPostponed%20%3A%20false&facets=%5B%5D&tagFilters=&facetFilters=%5B%22Venue.Name%3ACorner%20Hotel%22%5D"}]})

    # OR
    # r = requests.post('https://icgfyqwgtd-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.27.1%3Binstantsearch.js%201.12.1%3BJS%20Helper%202.26.0&x-algolia-application-id=ICGFYQWGTD&x-algolia-api-key=658602a6eeedca93a2ea1125e532f96f', json={"requests":[{"indexName":"prod_cornerhotel_eventguide","params":"query=&hitsPerPage=80&page=0&filters=IsCancelled%20%3A%20false%20AND%20IsPostponed%20%3A%20false&facets=%5B%5D&tagFilters=&facetFilters=%5B%22Venue.Name%3ACorner%20Hotel%22%5D"}]})

    json_r = r.json()

    print(json_r)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')


    s = soup.select("article.eventlist-event")
    
    for each in s:
        gig = { 
            "title": each.find(class_="eventlist-title-link").string,
            "description": "",
            "artists": [],
            "venue": "The Wesley Anne, Northcote",
            "when": "",
            "link": 'https://wesleyanne.com.au' + each.find(class_='eventlist-title-link')['href'],
            "genre": ""
        }
        for p in each.find_all(attrs={"style": "white-space:pre-wrap;"}):
            st = p.string
            if (st == None):
                st = "\n"
            holder = gig["description"]
            gig["description"] = holder + st
        when_string = each.find(class_='event-date').string + ' ' + each.find(class_="event-time-24hr-start").string
        gig["when"] = str(datetime.strptime(when_string, '%A, %d %B %Y %H:%M'))
        gigs_array.append(gig)

