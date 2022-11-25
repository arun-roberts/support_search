import requests
import json
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('http://affiliateapi.oztix.com.au/v1.9/JSRender.aspx?outlet_id=1495')

 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html')
 
s = soup.find_all("div", class_='JSRenderContainer')
 
gigs = []

for each in s:
    obj = { 
        "title": each.find(class_="JSRenderEventTitle").string,
        "description": "",
        "artists": [],
        "when": each.find(class_='JSRenderDate').string,
        "link": each.link.string,
        "sold_out": each.find('moshtix:soldout').string,
        "genre": each.genre.string
    }
    for artist in each.find('moshtix:artists'):
        str = artist.string
        if (str != "howler" and str != "hwlr" and str != "\n"):
            obj["artists"].append(str)
    gigs.append(obj)

print(gigs)

with open("hwlr_test.js", "w") as j:
    json.dump(gigs, j)  

# print(s)
# t = open("test.txt", "a")
# for line in lines:
#     # print(line.text)
#     t.write(str(line))
#     t.write(', ')
# t.close()
 
