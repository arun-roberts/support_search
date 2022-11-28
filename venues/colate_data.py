import json
import retreat as retreat
import croxton as croxton

gigs = []
retreat.gig_scraper(gigs)
croxton.scrape_gigs(gigs)
print(gigs)