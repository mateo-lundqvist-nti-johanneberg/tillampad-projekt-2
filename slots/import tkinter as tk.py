from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My First Tkinter Program")
root.geometry("500x500")

label=Label(root, text="", font=("Courier 22 bold"))
label.pack()

#Create an Entry widget to accept User Input

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#Create a Button to validate Entry Widget
ttk.Button(root, text= "Okay",width= 20, command= display_text).pack(pady=20)

root.mainloop()