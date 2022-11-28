import requests
import json
from bs4 import BeautifulSoup

def scrape_gigs(gigs_array):
    # Making a GET request
    r = requests.get('http://affiliateapi.oztix.com.au/v1.9/JSRender.aspx?outlet_id=1495')

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')


    s = soup.find_all("div", class_='JSRenderContainer')
    a = soup.find_all("a", class_='JSRenderEventTitle')
    hrefs = []
    for link in a:
        hrefs.append('https:' + link['href'])
    
    gigs = []

    for each in s:
        gig = { 
            "title": each.find(class_="JSRenderEventTitle").string,
            "description": "",
            "artists": [],
            "venue": each.find(class_="JSRenderVenueName").string,
            "when": each.find(class_='JSRenderDate').string,
            "link": 'https:' + each.find(class_='JSRenderEventTitle')['href'],
            "sold_out": "",
            "genre": ""
        }
        title = each.find(class_="JSRenderEventTitle").string
        supports = each.find(class_="JSRenderSpecialGuests").string or ""
        gig["artists"].append(title)
        gig["artists"].append(supports)
        gigs.append(gig)
        gigs_array.append(gig)
    return gigs



print(scrape_gigs([]))

# with open("hwlr_test.js", "w") as j:
#     json.dump(gigs, j)  

# print(s)
# t = open("test.txt", "a")
# for line in lines:
#     # print(line.text)
#     t.write(str(line))
#     t.write(', ')
# t.close()
 
