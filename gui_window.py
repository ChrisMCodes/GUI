#!/usr/bin/env

from tkinter import *

window = Tk()

window.title("This window is a GUI!")

# Sets and positions text in the window
lbl = Label(window, text="What is your name? ", font=("Arial", 20))
lbl.grid(column=0, row=0)


# Sizes the window
window.geometry('450x100')

# Creates an input field
txt = Entry(window, width=10)
txt.grid(column=1, row=0)

# Defines what to do when the user clicks
def clicked():
    res = "Welcome, " + txt.get()
    lbl.configure(text = res)
    
# Adds a button
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)

# Waits for user to interact
window.mainloop()
