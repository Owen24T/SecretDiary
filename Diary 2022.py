from os import getcwd
from tkinter import *
import datetime
import threading


PATH = "AppData\DiaryLogs.txt"
print(getcwd())

def myFun():
    result = myEntry1.get()
    addEntry(result)
    myLabel = Label(root, text=f"Success! Thanks for your entry!", font=("Calibri",10))
    myLabel.place(x=255, y=410)
    myEntry1.delete(first=0, last="end")
    num_entries = count_entries(date_str)
    
    if num_entries == 0:
        myLabel5 = Label(root, text=f'\nEntries made today: {num_entries}  ', fg="#D2042D", font=("Calibri", 15))
    else:
        myLabel5 = Label(root, text=f'\nEntries made today: {num_entries}  ', fg="#228B22", font=("Calibri", 15))
    
    myLabel5.place(x=255, y=164)

    last_entry = getLastEntry()
    myLabel7 = Label(root, text=f"Last entry: {last_entry}", fg="#0A1172", font=("Calibri", 12))
    myLabel7.place(x=198, y=218)

    t = threading.Timer(3, lambda: myLabel.destroy())
    t.start()


def addEntry(text):
    f = open(PATH, "a")
    d = datetime.datetime.now()

    if text.startswith("YESTERDAY: "):
        split_lst = text.split("YESTERDAY: ")
        entry_text = split_lst[1]
        delta1 = datetime.timedelta(days=1)
        d -= delta1
        dt = d.strftime(f"%A, {d.day} %B %Y -------: ")
    elif text.find(" DA: ") != -1:
        split_lst = text.split(" DA: ")
        num_DA = int(split_lst[0])
        entry_text = split_lst[1]
        delta1 = datetime.timedelta(days=num_DA)
        d -= delta1
        dt = d.strftime(f"%A, {d.day} %B %Y -------: ")
    else:
        entry_text = text
        dt = d.strftime(f"%A, {d.day} %B %Y %I:%M%p: ")
    message = dt + entry_text + "\n"
    f.write(message)
    f.close()


def count_entries(date_str):
    counter = 0
    f = open(PATH, "r")
    entry_list = f.readlines()
    for entry in entry_list:
        if entry.startswith(date_str):
            counter += 1
    f.close()
    return counter
    

def getLastEntry():
    f = open(PATH, "r")
    entry_list = f.readlines()
    last_str = entry_list[-1]
    position = last_str.find(": ")
    result = last_str[:position]
    return result

#####################################################################################################################################

root = Tk()
root.title("Diary 2022")
root.geometry("700x500")

date = datetime.date.today()
date_str = date.strftime(f"%A, {date.day} %B %Y")

myEntry1 = Entry(root, bd=3, width=100, bg="#D4D4D4", font=('Arial', 15))
myEntry1.place(relheight=0.3, relwidth=0.7, x=100, y=260)

myLabel2 = Label(root, text=f"Please make an entry for today \n{date_str}", fg="#2E5984", font=("Calibri", 25))
myLabel2.pack()

myLabel3 = Label(root, text='\nIf entering for yesterday, start with "YESTERDAY: " \n If entering for an earlier date, start with "<days> DA: "', fg="#528AAE", font=("Calibri", 15))
myLabel3.pack()

num_entries = count_entries(date_str)
if num_entries == 0:
    myLabel4 = Label(root, text=f'\nEntries made today: {num_entries}', fg="#D2042D", font=("Calibri", 15))
else:
    myLabel4 = Label(root, text=f'\nEntries made today: {num_entries}', fg="#228B22", font=("Calibri", 15))
myLabel4.pack()

last_entry = getLastEntry()
myLabel6 = Label(root, text=f"Last entry: {last_entry}", fg="#0A1172", font=("Calibri", 12))
myLabel6.pack()

myButton = Button(root, text="Add Entry", command=myFun, bd=5, height=1, width=7)
myButton.place(x=310, y=445)

root.mainloop()