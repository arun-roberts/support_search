import os
import subprocess
from tkinter import *
from tkinter import ttk

# def run():
#     os.system('python3 "compare_scrape_results.py"')
def run():
    subprocess.run(["python3", "compare_scrape_results.py"])

root = Tk()
frm = ttk.Frame(root, padding=15)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Check for new gigs", command=run).grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
root.mainloop()