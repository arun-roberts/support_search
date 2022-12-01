import json
import subprocess
from tkinter import *
from tkinter import ttk

with open("prev_scrape_results.json", "r") as prev_results:
    prev = json.load(prev_results)["data"]

# def run():
#     os.system('python3 "compare_scrape_results.py"')
def run():
    subprocess.run(["python3", "compare_scrape_results.py"])

root = Tk()
title_frame = ttk.Frame(root, padding=15)
title_frame.justify(CENTER)
ttk.Label(title_frame, text="Scrape it.")

info_body = ttk.Frame(root, padding=15)
info_body.grid()
for i, gig in enumerate(prev):
    ttk.Label(info_body, text=gig["title"]).grid(column=1, row=i)
    ttk.Button(info_body, text="Go fish", command=fish).grid(column=3, row=i)
    ttk.Button(info_body, text="Applied", command=checkItOff).grid(column=4, row=i)
    ttk.Button(info_body, text="No", command=getOutOfHere).grid(column=5, row=i)

ttk.Button(root, text="Exit", command=root.destroy)
root.mainloop()