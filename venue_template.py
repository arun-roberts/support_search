import requests
import json
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.moshtix.com.au/mosh2/rss/GenerateFeed.aspx?feedCode=636851343092690293')
h = requests.get('https://bprimal.com.au/collections/mens-shoes')

 
# Parsing the HTML
# soup = BeautifulSoup(r.content, 'xml')
soup = BeautifulSoup(h.content, 'html')
print(soup.find_all('div', "grid grid--uniform grid--view-items"))
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
 
