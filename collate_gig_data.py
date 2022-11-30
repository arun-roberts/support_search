import json
import venues.retreat as retreat 
import venues.croxton as croxton 
import venues.hwlr as hwlr
import venues.memo as memo
import venues.wesley_anne as wesley_anne

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
