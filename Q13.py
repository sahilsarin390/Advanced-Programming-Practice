from tkinter import *

root = Tk()

root.title("BookStore Management Software")
root.geometry("620x350")

e1 = Entry(root)
e1.grid(row=0, column=1)
e2 = Entry(root)
e2.grid(row=0, column=6)
e3 = Entry(root)
e3.grid(row=1, column=1)
e4 = Entry(root)
e4.grid(row=1, column=6)

list1 = Listbox(root, height=15, width=60,bd=4)
list1.grid(row=2, column =0, rowspan=10, columnspan=5,padx=10)

myLabel1 = Label(root, text ="Title")
myLabel1.grid(row=0, column=0,padx=10)
myLabel2 = Label(root, text ="Author")
myLabel2.grid(row=0, column=5,padx=10)
myLabel3 = Label(root, text ="Year")
myLabel3.grid(row=1, column=0,padx=10)
myLabel4 = Label(root, text ="ISBN")
myLabel4.grid(row=1, column=5,padx=10)

myButton1 = Button(root, text="View All", width=12,bd=3)
myButton1.grid(row=3, column=6,pady=4)
myButton2 = Button(root, text="Search", width=12,bd=3)
myButton2.grid(row=4, column=6)
myButton3 = Button(root, text="Add Entry", width=12,bd=3)
myButton3.grid(row=5, column=6,pady=10)
myButton4 = Button(root, text="Update Selected", width=12,bd=3)
myButton4.grid(row=6, column=6,pady=10)
myButton5 = Button(root, text="Delete Selected", width=12,bd=3)
myButton5.grid(row=7, column=6,pady=10)
myButton6 = Button(root, text="Close",command=root.destroy, width=12,bd=3)
myButton6.grid(row=8, column=6,pady=10)

root.mainloop()