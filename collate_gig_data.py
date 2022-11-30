import json
import retreat 
import croxton 
import hwlr
import memo
import wesley_anne

def scrape_it_all():
    gigs = []
    retreat.scrape_it(gigs)
    croxton.scrape_it(gigs)
    hwlr.scrape_it(gigs)
    memo.scrape_it(gigs)
    wesley_anne.scrape_it(gigs)

    as_obj = { "data": gigs }

    with open("new_scrape_results.json", "w") as j:
        json.dump(as_obj, j)  
