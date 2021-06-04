from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text=("Yo its clicked bitch!!")).pack()

myButton = Button(root, text=("Click Me!"), padx=50, pady=20, command = myClick, fg = "white", bg = "black").pack()

root.mainloop()