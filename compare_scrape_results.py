import json
from datetime import datetime
import collate_gig_data

collate_gig_data.scrape_it_all()

with open("prev_scrape_results.json", "r") as prev_results:
    prev = json.load(prev_results)["data"]

with open("new_scrape_results.json", "r") as new_results:
    new = json.load(new_results)["data"]

today = datetime.now()

for gig in prev:
    if (gig["when"] and datetime.strptime(gig["when"], "%Y-%m-%d %H:%M:%S" < today)):
        prev.remove(gig)

for each in new:
    unlisted = True
    for old in prev:
        if(each["title"] == old["title"]):
            unlisted = False
    if (unlisted == True):
        prev.append(each)

as_obj = { "data": prev }

with open("prev_scrape_results.json", "w") as j:
    json.dump(as_obj, j)  