from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import PIL
from PIL import ImageTk, Image

conn = sqlite3.connect('COVID19.db')
 
cursor = conn.cursor()

window=Tk()
window.title("COVID DETAILS")
window.geometry("440x550")
window.config(bg='white')

docs = Label(window,text="Total Number of Doctors",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=10)
e1 = Entry(window,width=20)
e1.place(x=270,y=10)

nurs = Label(window,text="Total Number of Nurses",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=50)
e2=Entry(window,width=20)
e2.place(x=270,y=50)

assis = Label(window,text="Total Number of Health Care Assistants",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=90)
e3=Entry(window,width=20)
e3.place(x=270,y=90)

bed = Label(window,text="Number of Beds in Covid 19 ward",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=130)
e4=Entry(window,width=20)
e4.place(x=270,y=130)


bedicu = Label(window,text="Number of Beds in Covid 19 ICU ward",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=170)
e5=Entry(window,width=20)
e5.place(x=270,y=170)

oxy = Label(window,text="Total Number of Oxygen Cylinders",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=210)
e6=Entry(window,width=20)
e6.place(x=270,y=210)

name = Label(window,text="Name of the person",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=250)
e7=Entry(window,width=20)
e7.place(x=270,y=250)

date = Label(window,text="Date of Vaccination",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=290)
e8=Entry(window,width=20)
e8.place(x=270,y=290)

aadh = Label(window,text="Aadhar Number",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=330)
e9=Entry(window,width=20)
e9.place(x=270,y=330)

dob = Label(window,text="Date of Birth",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=370)
e10=Entry(window,width=20)
e10.place(x=270,y=370)

age = Label(window,text="Age",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=410)
e11=Entry(window,width=20)
e11.place(x=270,y=410)

dose = Label(window,text="Dosage Count",font=("bold",10), bg="#aa4557", fg="#6edcdd").place(x=10,y=450)
e12=Entry(window,width=20)
e12.place(x=270,y=450)

cursor.execute("""CREATE TABLE readiness(
	e1 integer,
	e2 integer,
    e3 integer,
	e4 integer,
	e5 integer,
	e6 integer
	)""")

cursor.execute("""CREATE TABLE vaccination(
	e7 text,
	e8 integer, 
	e9 integer,
	e10 integer,
	e11 integer,
	e12 integer
	)""")


def update_data():
    conn = sqlite3.connect('COVID19.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO readiness VALUES(:e1, :e2, :e3, :e4, :e5, :e6)",
				  {
				     'e1': e1.get(),
				     'e2': e2.get(),
				     'e3': e4.get(),
                     'e4': e4.get(),
				     'e5': e5.get(),				     
				     'e6': e6.get()
				  })
                  
    cursor.execute("INSERT INTO vaccination VALUES(:e7, :e8, :e9, :e10, :e11, :e12)",
				  {
				     'e7': e7.get(),
				     'e8': e8.get(),
				     'e9': e9.get(),
                     'e10': e10.get(),
				     'e11': e11.get(),
				     'e12': e12.get()
				  })
    conn.commit()
    conn.close()

def details():
    newwindow = Tk()
    newwindow.title("Details")
    newwindow.geometry("900x300")

    conn = sqlite3.connect('COVID19.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT *, oid FROM readiness")
    details1 = cursor.fetchall()
    
    cursor.execute("SELECT *, oid FROM vaccination")
    details2 = cursor.fetchall()
    #print(details)
    print_details1 = ''
    for detail1 in details1:
        print_details1 +="\n"  +"Readiness Table" + "\n" + "Total Number of Doctors = " + str(detail1[0])  + "  |  " + "Total Number of Nurses = " + str(detail1[1])  + "  |  " + "Total Number of Health Care Assistants = " + str(detail1[2]) + "\n" + "Number of Beds in Covid 19 ward = " + str(detail1[3]) + "  |  " + "Number of Beds in Covid 19 ICU ward = " + str(detail1[4]) + "  |  " + "Total Number of Oxygen Cylinders = " + "Total Number of Ventilator Units = " + str(detail1[5]) + "\n"
    
    detail1_label = Label(newwindow, text=print_details1)
    detail1_label.place(x=1,y=25,anchor = W)

    print_details2 = ''
    for detail2 in details2:
        print_details2 +="\n" + "Vaccination Table" + "\n" + "Name of the person = " + str(detail2[0]) + "  |  " + "Date of Vaccination = " + str(detail2[1]) + "  |  " + "Aadhar Number = "  + str(detail2[2]) + "\n" + "  |  " + "Date of Birth = " + str(detail2[3]) + "  |  " +  "Age = " + str(detail2[4]) + "  |  " + "Dosage Count = " + str(detail2[5]) + "\n"

    
    detail2_label = Label(newwindow, text=print_details2)
    detail2_label.place(x=1,y=100, anchor = W)
    
    conn.commit()
    conn.close()
    newwindow.mainloop()
    
submitButton = Button(window, text="Submit", font=("bold",11), command=update_data, bg="#6edcdd", fg="#ab4c5c").place(x=120,y=510)
viewButton = Button(window, text="View Records", font=("bold",11), command=details, bg="#6edcdd", fg="#ab4c5c").place(x=200,y=510)
window.mainloop()