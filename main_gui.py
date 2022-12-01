import json
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

with open("prev_scrape_results.json", "r") as prev_results:
    prev = json.load(prev_results)["data"]

def run():
    subprocess.run(["python3", "compare_scrape_results.py"])

def fish():
    print("go fish")

def checkItOff(index):
    prev[index]["applied"] = True
    refresh()

def getOutOfHere(index, where):
    prev[index][where] = True
    print(prev[index][where])
    as_obj = {"data": prev}
    with open("prev_scrape_results.json", "w") as j:
        json.dump(as_obj, j)  
    refresh()

def refresh():
    root.destroy
    # subprocess.run(["python3", "main_gui.py"])
    root.mainloop()


root = Tk()
title_frame = ttk.Frame(root, padding=15, width=40, height=50)
# title_frame.justify(CENTER)
ttk.Label(title_frame, text="Scrape it.")


# info_body = ttk.Frame(root, padding=15)
info_body = ScrolledText(root, width=80, height= 18)
info_body.grid()
for i, gig in enumerate(prev):
    if (gig["applied"] == False and gig["uninterested"] == False):
        ttk.Label(info_body, text=gig["title"]).grid(column=1, row=i, sticky=W)
        ttk.Button(info_body, text="Go fish", command=fish).grid(column=3, row=i)
        ttk.Button(info_body, text="Applied", command=lambda: getOutOfHere(i, "applied")).grid(column=4, row=i)
        ttk.Button(info_body, text="No", command=lambda: getOutOfHere(i, "uninterested")).grid(column=5, row=i)

ttk.Button(root, text="Exit", command=root.destroy)
root.mainloop()