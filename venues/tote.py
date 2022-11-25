import requests
import json
from bs4 import BeautifulSoup

# Making a GET request
r = requests.post('https://icgfyqwgtd-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20vanilla%20JavaScript%20(lite)%203.27.1%3Binstantsearch.js%201.12.1%3BJS%20Helper%202.26.0&x-algolia-application-id=ICGFYQWGTD&x-algolia-api-key=26074ac519e5a12673bebf428d0ffe49',
params={"query": "", "hitsPerPage": "40", "page": "0", "filters": "IsCancelled%20%3A%20false%20AND%20IsPostponed%20%3A%20false", "facets": "%5B%5D", "tagFilters": ""})

print(r);
 
# Parsing the HTML
# soup = BeautifulSoup(r.content, 'xml')
 
# s = soup.find_all('item')
 
# gigs = []

# for each in s:
#     obj = { 
#         "title": each.title.string,
#         "description": each.description.string,
#         "artists": [],
#         "when": each.find('moshtix:eventstartdatetime').string,
#         "link": each.link.string,
#         "sold_out": each.find('moshtix:soldout').string,
#         "genre": each.genre.string
#     }
#     for artist in each.find('moshtix:artists'):
#         str = artist.string
#         if (str != "howler" and str != "hwlr" and str != "\n"):
#             obj["artists"].append(str)
#     gigs.append(obj)

# print(gigs)

# with open("hwlr_test.js", "w") as j:
#     json.dump(gigs, j)  

# print(s)
# t = open("test.txt", "a")
# for line in lines:
#     # print(line.text)
#     t.write(str(line))
#     t.write(', ')
# t.close()
 
