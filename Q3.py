from tkinter import *

root = Tk()
root.title("Employee Details")
root.geometry("330x180+30+30")

r = IntVar()

Radiobutton(root, text="Regular", variable=r,value=1).grid(row=3,column=1)
Radiobutton(root, text="Temporary", variable=r,value=2).grid(row=3,column=2)

w = Spinbox(root, from_=1, to=100).grid(row=4,column=1)

e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)
e3 = Entry(root)
e3.grid(row=2, column=1)

myLabel1 = Label(root, text ="Empid")
myLabel1.grid(row=0, column=0)
myLabel2 = Label(root, text ="Employee Name:")
myLabel2.grid(row=1, column=0)
myLabel3 = Label(root, text ="Job")
myLabel3.grid(row=2, column=0)
myLabel4 = Label(root, text ="Employee type")
myLabel4.grid(row=3, column=0)
myLabel5 = Label(root, text ="Salary")
myLabel5.grid(row=4, column=0)

myButton1 = Button(root, text="Insert")
myButton1.grid(row=5, column=0)
myButton2 = Button(root, text="Delete")
myButton2.grid(row=6, column=0)
myButton3 = Button(root, text="Update")
myButton3.grid(row=5, column=1)
myButton4 = Button(root, text="Select")
myButton4.grid(row=6, column=1)

root.mainloop()