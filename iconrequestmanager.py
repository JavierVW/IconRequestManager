import os
import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from collections import defaultdict
from collections import OrderedDict

root = tk.Tk()
root.title("Icon Request Manager")

appList = defaultdict(int)
appListNames = defaultdict(int)

appNames = []
appNames2 = []

appCount = []
appCount2 = []


def addFolder():
    appList.clear()
    appListNames.clear()

    appNames.clear()
    appNames2.clear()
    appCount.clear()
    appCount2.clear()

    for item in treeNames.get_children():
        treeNames.delete(item)


    filename = filedialog.askdirectory(title="Select folder")
    if filename is not None:
        for files in os.listdir(filename):
            if files.endswith('.xml'):
                filedata = filename + "/" + files
                with open(filedata, 'r', encoding="utf-8") as content:
                    tree = ET.parse(content)
                    list_class = tree.findall("item")
                    for appdata in list_class:
                        appList[appdata.get("class")] += 1
                        appListNames[appdata.get("name")] += 1

        for w in sorted(appList, key=appList.get, reverse=True):
            appNames.append(w)
            appCount.append(appList[w])

        for w in sorted(appListNames, key=appListNames.get, reverse=True):
            appNames2.append(w)
            appCount2.append(appListNames[w])

        for app, name, req in zip(appNames, appNames2, appCount):
            if app is not None:
                treeNames.insert(parent='', index="end", values=(app, name, req))
                treeNames.grid(column=0, row=0)


frame = Frame(root)
scrollBar = Scrollbar(frame, orient=VERTICAL)

appCountListBox = Listbox(frame, width=5)


scrollBar.grid(column=1, row=0, sticky="ns")

treeNames = ttk.Treeview(frame, yscrollcommand=scrollBar.set, selectmode="browse")
treeNames['columns'] = ("App", "Names", "Requests")

treeNames.column("#0", width=0, stretch=NO)
treeNames.column("App", anchor=W, width=300, minwidth=300)
treeNames.column("Names", anchor=W, width=300, minwidth=300)
treeNames.column("Requests", anchor=W, width=120, minwidth=100)

treeNames.heading("#0")
treeNames.heading("App", text="Apps", anchor=W)
treeNames.heading("Names", text="Names", anchor=W)
treeNames.heading("Requests", text="Requests", anchor=W)
scrollBar.config(command=treeNames.yview)
treeNames.grid(column=0, row=0)



openFolder = tk.Button(root, text="Select folder", command=addFolder)


frame.grid(padx=10, pady=10)
openFolder.grid(column=0, row=2, padx=10, pady=5)


root.mainloop()
