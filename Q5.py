from tkinter import *

root = Tk()
root.title("Employee Details")
root.geometry("460x200+30+30")

r = IntVar()
vara=IntVar()
varb=IntVar()

Radiobutton(root, text="A", variable=r,value=1).grid(row=3,column=1)
Radiobutton(root, text="B", variable=r,value=2).grid(row=3,column=2)

c=Checkbutton(root, text="7:15PM", variable=vara).grid(row=3,column=5)

d=Checkbutton(root, text="9AM", variable=varb).grid(row=3,column=6)

w = Scale(root, from_=0, to=10, orient=HORIZONTAL).grid(row=4,column=1)

e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=1, column=1)
e3 = Entry(root)
e3.grid(row=2, column=1)

myLabel1 = Label(root, text ="Movie Booking id")
myLabel1.grid(row=0, column=0)
myLabel2 = Label(root, text ="Person Name:")
myLabel2.grid(row=1, column=0)
myLabel3 = Label(root, text ="Movie Name")
myLabel3.grid(row=2, column=0)
myLabel4 = Label(root, text ="Class")
myLabel4.grid(row=3, column=0)
myLabel5 = Label(root, text ="No. of Tickets")
myLabel5.grid(row=4, column=0)
myLabel6= Label(root, text ="Time of Show")
myLabel6.grid(row=3, column=4)

myButton1 = Button(root, text="Insert")
myButton1.grid(row=5, column=0)
myButton2 = Button(root, text="Delete")
myButton2.grid(row=6, column=0)
myButton3 = Button(root, text="Update")
myButton3.grid(row=5, column=1)
myButton4 = Button(root, text="Select")
myButton4.grid(row=6, column=1)

root.mainloop()