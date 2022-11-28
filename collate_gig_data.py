import json
import venues.retreat as retreat
import venues.croxton as croxton
import venues.hwlr as hwlr

def scrape_it_all():
    gigs = []
    retreat.gig_scraper(gigs)
    croxton.scrape_it(gigs)
    hwlr.scrape_it(gigs)

    as_obj = { "data": gigs }

    with open("new_scrape_results.json", "w") as j:
        json.dump(as_obj, j)  
