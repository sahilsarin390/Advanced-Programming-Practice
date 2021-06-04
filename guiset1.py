from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('studentregform.db')
 
cursor = conn.cursor()
'''
cursor.execute("""CREATE TABLE form(
	e1 text,
	e2 text,
	drop1 text,
	drop2 text,
	drop3 text,
	e4 text,
	e5 integer,
	r integer,
	e6 text,
	e7 text,
	e8 integer, 
	e9 text,
	e10 text,
	varc integer,
	vard integer,
	vare integer,
	varf integer,
	varg integer,
	e23 text,
	e11 text,
	e12 text,
	e13 text,
	e14 text,
	e15 real,
	e16 real,
	e17 real,
	e18 real,
	e19 integer,
	e20 integer,
	e21 integer,
	e22 integer,
	t integer
	)""")
'''
root = Tk()
root.title("STUDENT REGISTRATION FORM")
root.configure(bg="#7303fc")
root.geometry("860x700")

fname = Label(root, bg="#7303fc", fg="white",text="FIRST NAME")
fname.grid(row=0, column=0, padx=5, pady=6, sticky=W)
e1 = Entry(root)
e1.grid(row=0, column=1, padx=2, pady=6)
fazmax = Label(root, bg="#7303fc", fg="white",text="(max 30 characters a-z and A-Z)", anchor =E)
fazmax.grid(row=0, column=2)

lname = Label(root, bg="#7303fc", fg="white",text="LAST NAME")
lname.grid(row=1, column=0, padx=5, pady=6, sticky=W)
e2 = Entry(root)
e2.grid(row=1, column=1, padx=2, pady=6)
lazmax = Label(root, bg="#7303fc", fg="white",text="(max 30 characters a-z and A-Z)")
lazmax.grid(row=1, column=2)

dob = Label(root, bg="#7303fc", fg="white",text="DATE OF BIRTH")
dob.grid(row=2, column=0, padx=5, pady=6, sticky=W)

options1=["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18","19", "20","21","22", "23", "24", "25", "26", "27", "28","29", "30", "31"]
options2=["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
options3=["1998","1999", "2000", "2001", "2002", "2003", "2004"]
drop1 = ttk.Combobox(root, value=options1, width=11)
drop1.set("Day")
drop1.grid(row=2, column=1, sticky=E)
drop2 = ttk.Combobox(root, value=options2, width=10)
drop2.set("Month")
drop2.grid(row=2, column=2)
drop3 = ttk.Combobox(root, value=options3, width=5)
drop3.set("Year")
drop3.grid(row=2, column=3, sticky=W)

mail = Label(root, bg="#7303fc", fg="white",text="EMAIL ID")
mail.grid(row=3, column=0, padx=5, pady=6, sticky=W)
e4 = Entry(root)
e4.grid(row=3, column=1, padx=2, pady=6)

nmb = Label(root, bg="#7303fc", fg="white",text="MOBILE NUMBER")
nmb.grid(row=4, column=0, padx=5, pady=6, sticky=W)
e5 = Entry(root)
e5.grid(row=4, column=1, padx=2, pady=6)
tendig = Label(root, bg="#7303fc", fg="white",text="(10-digit number)")
tendig.grid(row=4, column=2, sticky=W)

gen = Label(root, bg="#7303fc", fg="white",text="GENDER")
gen.grid(row=5, column=0, padx=5, pady=6, sticky=W)

r = IntVar()
r1 = Radiobutton(root, bg="#7303fc",text="Male", variable=r,value=1)
r1.grid(row=5,column=1, sticky=W)
r2 = Radiobutton(root, bg="#7303fc",text="Female", variable=r,value=2)
r2.grid(row=5,column=2, sticky=W)

address = Label(root, bg="#7303fc", fg="white",text="ADDRESS")
address.grid(row=6, column=0, padx=5, pady=6, sticky=W)
e6 = tk.Text(root, width=16, height=4)
e6.grid(row=6, column=1, padx=2, pady=6)

city = Label(root, bg="#7303fc", fg="white",text="CITY")
city.grid(row=7, column=0, padx=5, pady=6, sticky=W)
e7 = Entry(root)
e7.grid(row=7, column=1, padx=2, pady=6)
amax = Label(root, bg="#7303fc", fg="white",text="(max 30 characters a-z and A-Z)")
amax.grid(row=7, column=2)

pin = Label(root, bg="#7303fc", fg="white",text="PINCODE")
pin.grid(row=8, column=0, padx=5, pady=6, sticky=W)
e8 = Entry(root)
e8.grid(row=8, column=1, padx=2, pady=6)
dig = Label(root, bg="#7303fc", fg="white",text="(6-digit number)")
dig.grid(row=8, column=2, sticky=W)

state = Label(root, bg="#7303fc", fg="white",text="STATE")
state.grid(row=9, column=0, padx=5, pady=6, sticky=W)
e9 = Entry(root)
e9.grid(row=9, column=1, padx=2, pady=6)
azmax = Label(root, bg="#7303fc", fg="white",text="(max 30 characters a-z and A-Z)")
azmax.grid(row=9, column=2)

cntry = Label(root, bg="#7303fc", fg="white",text="COUNTRY")
cntry.grid(row=10, column=0, padx=5, pady=6, sticky=W)
e10 = Entry(root)
e10.grid(row=10, column=1, padx=2, pady=6)

hbbs = Label(root, bg="#7303fc", fg="white",text="HOBBIES")
hbbs.grid(row=11, column=0, padx=5, pady=6, sticky=W)

varc = IntVar()
vard = IntVar()
vare = IntVar()
varf = IntVar()
varg = IntVar()

c=Checkbutton(root, bg="#7303fc",text="Drawing", variable=varc)
c.grid(row=11,column=1, sticky=E)
d=Checkbutton(root, bg="#7303fc",text="Singing", variable=vard)
d.grid(row=11,column=2)
e=Checkbutton(root, bg="#7303fc",text="Dancing", variable=vare)
e.grid(row=11,column=3)
f=Checkbutton(root, bg="#7303fc",text="Sketching", variable=varf)
f.grid(row=11,column=4)
g=Checkbutton(root, bg="#7303fc",text="Others", variable=varg)
g.grid(row=12,column=1, sticky=E)
e23 = Entry(root)
e23.grid(row=12, column=2, sticky=W)

qual = Label(root, bg="#7303fc", fg="white",text="QUALIFICATION")
qual.grid(row=13, column=0, padx=5, pady=6, sticky=W)

sn = Label(root, bg="#7303fc", fg="white",text="S.No.")
sn.grid(row=13, column=1, sticky=E)
n1 = Label(root, bg="#7303fc", fg="white",text="1")
n1.grid(row=14, column=1, sticky=E)
n2= Label(root, bg="#7303fc", fg="white",text="2")
n2.grid(row=15, column=1, sticky=E)
n3 = Label(root, bg="#7303fc", fg="white",text="3")
n3.grid(row=16, column=1, sticky=E)
n4 = Label(root, bg="#7303fc", fg="white",text="4")
n4.grid(row=17, column=1, sticky=E)

exam = Label(root, bg="#7303fc", fg="white",text="Examination")
exam.grid(row=13, column=2)
ten = Label(root, bg="#7303fc", fg="white",text="Class X")
ten.grid(row=14, column=2)
twelve = Label(root, bg="#7303fc", fg="white",text="Class XII")
twelve.grid(row=15, column=2)
grad = Label(root, bg="#7303fc", fg="white",text="Graduation")
grad.grid(row=16, column=2)
master = Label(root, bg="#7303fc", fg="white",text="Masters")
master.grid(row=17, column=2)

brd = Label(root, bg="#7303fc", fg="white",text="Board")
brd.grid(row=13, column=3)
e11 = Entry(root)
e11.grid(row=14, column=3, padx=2, pady=2)
e12 = Entry(root)
e12.grid(row=15, column=3, padx=2, pady=2)
e13 = Entry(root)
e13.grid(row=16, column=3, padx=2, pady=2)
e14 = Entry(root)
e14.grid(row=17, column=3, padx=2, pady=2)
chmax = Label(root, bg="#7303fc", fg="white",text="(10 char max)")
chmax.grid(row=18, column=3)

page = Label(root, bg="#7303fc", fg="white",text="Percentage")
page.grid(row=13, column=4)
e15 = Entry(root)
e15.grid(row=14, column=4, padx=2, pady=2)
e16 = Entry(root)
e16.grid(row=15, column=4, padx=2, pady=2)
e17 = Entry(root)
e17.grid(row=16, column=4, padx=2, pady=2)
e18 = Entry(root)
e18.grid(row=17, column=4, padx=2, pady=2)
decmax = Label(root, bg="#7303fc", fg="white",text="(upto 2 decimal)")
decmax.grid(row=18, column=4)

passin =  Label(root, bg="#7303fc", fg="white",text="Year of Passing")
passin.grid(row=13, column=5)
e19 = Entry(root)
e19.grid(row=14, column=5, padx=2, pady=2)
e20 = Entry(root)
e20.grid(row=15, column=5, padx=2, pady=2)
e21 = Entry(root)
e21.grid(row=16, column=5, padx=2, pady=2)
e22 = Entry(root)
e22.grid(row=17, column=5, padx=2, pady=2)

course = Label(root, bg="#7303fc", fg="white",text="COURSES APPLIED FOR", wraplength=80)
course.grid(row=19, column=0, padx=5, pady=6, sticky=W)

t = IntVar()
r3 = Radiobutton(root, bg="#7303fc",text="BCA", variable=t,value=1)
r3.grid(row=19,column=1)
r4 = Radiobutton(root, bg="#7303fc",text="B.Com", variable=t,value=2)
r4.grid(row=19,column=2)
r5 = Radiobutton(root, bg="#7303fc",text="B.Sc", variable=t,value=3)
r5.grid(row=19,column=3)
r6 = Radiobutton(root, bg="#7303fc",text="B.A", variable=t,value=4)
r6.grid(row=19,column=4)

def submission():
	conn = sqlite3.connect('studentregform.db')
	cursor = conn.cursor()

	cursor.execute("INSERT INTO form VALUES(:e1, :e2, :drop1, :drop2, :drop3, :e4, :e5, :r, :e6, :e7, :e8, :e9, :e10, :varc, :vard, :vare, :varf, :varg, :e23, :e11, :e12, :e13, :e14, :e15, :e16, :e17, :e18, :e19, :e20, :e21, :e22, :t)",
				  {
				     'e1': e1.get(),
				     'e2': e2.get(),
				     'drop1': drop1.get(),
				     'drop2': drop2.get(),
				     'drop3': drop3.get(),
				     'e4': e4.get(),
				     'e5': e5.get(),
				     'r': r.get(),
				     'e6': e6.get(1.0,END),
				     'e7': e7.get(),
				     'e8': e8.get(),
				     'e9': e9.get(),
				     'e10': e10.get(),
				     'varc': varc.get(),
				     'vard': vard.get(),
				     'vare': vare.get(),
				     'varf': varf.get(),
				     'varg': varg.get(),
				     'e23': e23.get(),
				     'e11': e11.get(),
				     'e12': e12.get(),
				     'e13': e13.get(),
				     'e14': e14.get(),
				     'e15': e15.get(),
				     'e16': e16.get(),
				     'e17': e17.get(),
				     'e18': e18.get(),
				     'e19': e19.get(),
				     'e20': e20.get(),
				     'e21': e21.get(),
				     'e22': e22.get(),
				     't': t.get()
				  })

	conn.commit()
	conn.close()
	print ('Your Registration is Successfull!!')
	messagebox.showinfo("Submission Successfull", "Your Registration is Successfull!!")

MyButton1 = Button(root, text="Submit", width=10, command=submission)
MyButton1.grid(row=20, column=2)

def resetting():
	e1.delete(0, END)
	e2.delete(0, END)
	drop1.set("Day")
	drop2.set("Month")
	drop3.set("Year")
	e4.delete(0, END)
	e5.delete(0, END)
	r.set(0)
	e6.delete(1.0, END)
	e7.delete(0, END)
	e8.delete(0, END)
	e9.delete(0, END)
	e10.delete(0, END)
	varc.set(0)
	vard.set(0)
	vare.set(0)
	varf.set(0)
	varg.set(0)
	e23.delete(0, END)
	e11.delete(0, END)
	e12.delete(0, END)
	e13.delete(0, END)
	e14.delete(0, END)
	e15.delete(0, END)
	e16.delete(0, END)
	e17.delete(0, END)
	e18.delete(0, END)
	e19.delete(0, END)
	e20.delete(0, END)
	e21.delete(0, END)
	e22.delete(0, END)
	t.set(0)

	print ('The form has been successfully reset.')
	messagebox.showinfo("Resetting Successfull", "The form has been successfully reset.")

MyButton2 = Button(root, text="Reset", width=10, command=resetting)
MyButton2.grid(row=20, column=3)


def details():
	window = Tk()
	window.title("Details")
	window.configure(bg="#7303fc")
	window.geometry("600x300")

	conn = sqlite3.connect('studentregform.db')
	cursor = conn.cursor()

	cursor.execute("SELECT *, oid FROM form")
	details = cursor.fetchall()
	#print(details)

	print_details = ''
	for detail in details:
		print_details += str(detail[0]) + " " + str(detail[1]) + " " + str(detail[2]) + " " + str(detail[3]) + " " + str(detail[4]) + " " + str(detail[5]) + " " + str(detail[6]) + " " + str(detail[7]) + " " + str(detail[8]) + " " + str(detail[9]) + " " + str(detail[10]) + " " + str(detail[11]) + " " + str(detail[12]) + " " + str(detail[13]) + " " + str(detail[14]) + " " + str(detail[15]) + " " + str(detail[16]) + " " + str(detail[17]) + " " + str(detail[18]) + " " + str(detail[19]) + " " + str(detail[20]) + " " + str(detail[21]) + " " + str(detail[22]) + " " + str(detail[23]) + " " + str(detail[24]) + " " + str(detail[25]) + " " + str(detail[26]) + " " + str(detail[27]) + " " + str(detail[28]) + " " + str(detail[29]) + " " + str(detail[30]) + " " + str(detail[31]) + "\n"

	detail_label = Label(window, bg="#7303fc", fg="white", text=print_details)
	detail_label.grid(row=0, column=0, columnspan=4, padx=4, pady=2)

	conn.commit()

	conn.close()

	window.mainloop()



MyButton3 = Button(root, text ="View Details", width=10, command=details)
MyButton3.grid(row=20, column=4, padx=45)

conn.commit()

conn.close()

root.mainloop()