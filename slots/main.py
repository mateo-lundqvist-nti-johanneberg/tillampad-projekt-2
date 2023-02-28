from csv import excel_tab
from operator import contains
import sqlite3
from argon2 import PasswordHasher
from tkinter import *
from tkinter import ttk
import random

slotOptions = ["7 ", "<3 ", "BAR ", "BELL ", ">-8 ", "-O ", "D "]

global coins
coins = 0

jackpot = "7 7 7 "
BigPot = ["<3 <3 <3 ", "BAR BAR BAR ", "BELL BELL BELL ", ">-8 >-8 >-8 ", "-O -O -O ", "D D D "]


global active_user
active_user = ""

def raise_frame(frame):
    frame.tkraise()


ph = PasswordHasher()

root = Tk()

root1 = Toplevel()

root1.geometry("1920x1080")

f1 = Frame(root1)
f2 = Frame(root1)
f3 = Frame(root1)

for frame in (f1, f2, f3):
    frame.pack()

con = sqlite3.connect("db.db")
cur = con.cursor()

def end():
    global coins
    cur.execute("UPDATE thing SET money = ? WHERE user = ?", (coins, active_user))
    con.commit()
    root.destroy()

def createAcc():
    global active_user
    global coins
    password = newPass.get()
    usernameNew = newUser.get()
    hashed_password = ph.hash(password)
    cur.execute("INSERT INTO thing (user, money, password) VALUES (?,?,?)", (usernameNew, 10000, hashed_password))
    con.commit()
    active_user = usernameNew
    coins = 10000
    main()

def login():
    global entryUsername
    global entryPass

    label = Label(f2, text="Enter username and password", font=("Courier 22 bold"))
    label.pack(padx=0, pady=10)

    entryUsername = Entry(f2, width= 40)
    entryUsername.focus_set()
    entryUsername.pack(padx=0, pady=10)

    entryPass = Entry(f2, width= 40)
    entryPass.focus_set()
    entryPass.pack()

    ttk.Button(f2, text= "Enter",width= 20, command=loginCheck).pack(pady=20)
    raise_frame(f2)

def create():
    global newUser
    global newPass

    label = Label(f3, text="Create username and password", font=("Courier 22 bold"))
    label.pack(padx=0, pady=10)

    newUser = Entry(f3, width= 40)
    newUser.focus_set()
    newUser.pack(padx=0, pady=10)

    newPass = Entry(f3, width= 40)
    newPass.focus_set()
    newPass.pack()

    ttk.Button(f3, text= "Enter",width= 20, command=createAcc).pack(pady=20)
    raise_frame(f3)

def loginCheck():
    global username
    global active_user
    global coins
    i = 0
    password = entryPass.get()
    username = entryUsername.get()
    cur.execute("SELECT * FROM thing")
    data = cur.fetchall()
    try:
        while i < len(data):
            if data[i][0] == username and ph.verify(data[i][2], password) == True:
                active_user = username
                coins = data[i][1]
                main()
            else:
                i += 1
                print("Invalid username or password, please try again")
    except:
        print("shit dont work bru")

def roll():
    global root2
    global coins
    wintext = ""
    coins = coins - 10
    slot1 = random.choice(slotOptions)
    slot2 = random.choice(slotOptions)
    slot3 = random.choice(slotOptions)
    final = slot1 + slot2 + slot3
    alreadywon = False
    if final == "7 7 7 ":
        wintext = "Jackpot!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        coins = coins + (10*100)
        alreadywon = True
    for x in BigPot:
        if final == x and alreadywon == False:
            wintext = "Bigpot"
            coins = coins + (10*10)
            alreadywon = True
    if final.split(" ")[0] == final.split(" ")[1] and alreadywon == False or final.split(" ")[1] == final.split(" ")[2] and alreadywon == False:
        wintext = "At least you got double back"
        coins = coins + (10*2)
        alreadywon = True
    if root2 is not None:
        root2.destroy()
    root2 = Toplevel()
    root2.geometry("1920x1080")
    Label(root2, text=final, font=("Courier 22 bold")).pack()
    Label(root2, text=wintext, font=("Courier 22 bold")).pack()
    Label(root2, text=f"You have {coins} coins left", font=("Courier 22 bold")).pack()
    ttk.Button(root2, text="Roll again", width=20, command=roll).pack(pady=40)
    ttk.Button(root2, text="Roll 50 coins", width=20, command=roll50).pack(pady=40)
    ttk.Button(root2, text="Roll 100 coins", width=20, command=roll100).pack(pady=40)
    ttk.Button(root2, text="Exit", width=20, command=end).pack(pady=40)

def roll50():
    global root2
    global coins
    wintext = ""
    coins = coins - 50
    slot1 = random.choice(slotOptions)
    slot2 = random.choice(slotOptions)
    slot3 = random.choice(slotOptions)
    final = slot1 + slot2 + slot3
    alreadywon = False
    if final == "7 7 7 ":
        wintext = "Jackpot"
        coins = coins + (50*100)
        alreadywon = True
    for x in BigPot:
        if final == x and alreadywon == False:
            wintext = "Bigpot"
            coins = coins + (50*10)
            alreadywon = True
    if final.split(" ")[0] == final.split(" ")[1] and alreadywon == False or final.split(" ")[1] == final.split(" ")[2] and alreadywon == False:
        wintext = "At least you got double back"
        coins = coins + (50*2)
        alreadywon = True
    if root2 is not None:
        root2.destroy()
    root2 = Toplevel()
    root2.geometry("1920x1080")
    Label(root2, text=final, font=("Courier 22 bold")).pack()
    Label(root2, text=wintext, font=("Courier 22 bold")).pack()
    Label(root2, text=f"You have {coins} coins left", font=("Courier 22 bold")).pack()
    ttk.Button(root2, text="Roll again", width=20, command=roll).pack(pady=40)
    ttk.Button(root2, text="Roll 50 coins", width=20, command=roll50).pack(pady=40)
    ttk.Button(root2, text="Roll 100 coins", width=20, command=roll100).pack(pady=40)
    ttk.Button(root2, text="Exit", width=20, command=end).pack(pady=40)

def roll100():
    global root2
    global coins
    wintext = ""
    coins = coins - 100
    slot1 = random.choice(slotOptions)
    slot2 = random.choice(slotOptions)
    slot3 = random.choice(slotOptions)
    final = slot1 + slot2 + slot3
    alreadywon = False
    if final == "7 7 7 ":
        wintext = "Jackpot"
        coins = coins + (100*100)
        alreadywon = True
    for x in BigPot:
        if final == x and alreadywon == False:
            wintext = "Bigpot"
            coins = coins + (100*10)
            alreadywon = True
    if final.split(" ")[0] == final.split(" ")[1] and alreadywon == False or final.split(" ")[1] == final.split(" ")[2] and alreadywon == False:
        wintext = "At least you got double back"
        coins = coins + (100*2)
        alreadywon = True
    if root2 is not None:
        root2.destroy()
    root2 = Toplevel()
    root2.geometry("1920x1080")
    Label(root2, text=final, font=("Courier 22 bold")).pack()
    Label(root2, text=wintext, font=("Courier 22 bold")).pack()
    Label(root2, text=f"You have {coins} coins left", font=("Courier 22 bold")).pack()
    ttk.Button(root2, text="Roll again", width=20, command=roll).pack(pady=40)
    ttk.Button(root2, text="Roll 50 coins", width=20, command=roll50).pack(pady=40)
    ttk.Button(root2, text="Roll 100 coins", width=20, command=roll100).pack(pady=40)
    ttk.Button(root2, text="Exit", width=20, command=end).pack(pady=40)

def main():
    global root2
    global root1
    if root1 is not None:
        root1.destroy()
    root2 = Toplevel()
    root2.geometry("1920x1080")
    Label(root2, text="Press roll to roll the slots", font=("Courier 22 bold")).pack(pady=20)
    Label(root2, text="Every roll costs 100 coins", font=("Courier 22 bold")).pack(pady=20)
    Label(root2, text=f"You have {coins} coins", font=("Courier 22 bold")).pack(pady=20)
    ttk.Button(root2, text="Roll 10 coins", width=20, command=roll).pack(pady=40)
    ttk.Button(root2, text="Roll 50 coins", width=20, command=roll50).pack(pady=40)
    ttk.Button(root2, text="Roll 100 coins", width=20, command=roll100).pack(pady=40)
    ttk.Button(root2, text="Exit", width=20, command=end).pack(pady=40)
    root2.mainloop()


def mainScreen():
    label = Label(f1, text="Welcome to epic gambling thing!", font=("Courier 22 bold"))
    label.pack(padx=0, pady=10)
    ttk.Button(f1, text= "Login",width= 20, command=login).pack(pady=20)
    raise_frame(f1)
    ttk.Button(f1, text= "Create Account",width= 20, command=create).pack(pady=20)

mainScreen()
root1.mainloop()
