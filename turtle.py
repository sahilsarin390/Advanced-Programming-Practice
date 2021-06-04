from tkinter import*
import tkinter as tk
root = Tk()
root.geometry("1920x1080")
root.title("STUDENT REGISTRATION FORM")

a = Label(root, text="STUDENT REGISTRATION FORM", font=("bold",20,"underline"), bg="white", fg="Purple").pack()
root.configure(background="Purple");


label1 = Label(root, text = "FIRST NAME", bg = "Purple", fg = "White")
label1.place(x = 10, y = 40)

entry1 = Entry(root, width = 40)
entry1.place(x = 120, y = 40)

label1c = Label(root, text="(max 30 characters a-z and A-Z)", bg = "Purple", fg = "White")
label1c.place(x = 370, y = 40)

label2 = Label(root, text = "LAST NAME", bg = "Purple", fg = "White")
label2.place(x = 10, y = 70)

entry2 = Entry(root, width = 40)
entry2.place(x = 120, y =70)

label2c = Label(root, text="(max 30 characters a-z and A-Z)", bg = "Purple", fg = "White")
label2c.place(x = 370, y = 70)

label3 = Label(text = "DATE OF BIRTH", bg = "Purple", fg = "White")
label3.place(x = 10, y = 100)

day = StringVar()
month = StringVar()
year = StringVar()

day.set("Day")
drop = OptionMenu(root , day , 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
drop.place(x = 120, y = 100)

month.set("Month")
drop = OptionMenu(root , month , "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "November", "December")
drop.place(x = 240, y = 100)

year.set("Year")
drop = OptionMenu(root , year , 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)
drop.place(x = 360, y = 100)

label4 = Label(text = "EMAIL ID", bg = "Purple", fg = "White")
label4.place(x = 10, y = 150)

entry4 = Entry(root, width = 40)
entry4.place(x = 120, y =150)

label5 = Label(root, text = "MOBILE NUMBER", bg = "Purple", fg = "White")
label5.place(x = 10, y = 180)

entry5 = Entry(root, width = 40)
entry5.place(x = 120, y =180)

label5c = Label(root, text="(10 digit number)", bg = "Purple", fg = "White")
label5c.place(x = 370, y = 180)

label6 = Label(root, text = "GENDER", bg = "Purple", fg = "White")
label6.place(x = 10, y = 210)

v1 = IntVar()
R1 = Radiobutton(root , text = "Male", variable = v1, value = 1, bg = "Purple").place(x = 120, y = 210)

v2 = IntVar()
R2 = Radiobutton(root , text = "Female", variable = v1, value = 2, bg = "Purple").place(x = 200, y = 210)

label7 = Label(root, text = "ADDRESS", bg = "Purple", fg = "White")
label7.place(x = 10, y = 240)

entry7 = Entry(root, width = 70)
entry7.place(x = 120, y = 240, height = 40)

label8 = Label(root, text = "CITY", bg = "Purple", fg = "White")
label8.place(x = 10, y = 300)

entry8 = Entry(root, width = 40)
entry8.place(x = 120, y = 300)

label8c = Label(root, text="(max 30 characters a-z and A-Z)", bg = "Purple", fg = "White")
label8c.place(x = 370, y = 300)

label9 = Label(root, text = "PIC CODE", bg = "Purple", fg = "White")
label9.place(x = 10, y = 330)

entry9 = Entry(root, width = 40)
entry9.place(x = 120, y = 330)

label9c = Label(root, text="(6 digit number)", bg = "Purple", fg = "White")
label9c.place(x = 370, y = 330)

label10 = Label(root, text = "STATE", bg = "Purple", fg = "White")
label10.place(x = 10, y = 360)

entry10 = Entry(root, width = 40)
entry10.place(x = 120, y = 360)

label10c = Label(root, text="(max 30 characters a-z and A-Z)", bg = "Purple", fg = "White")
label10c.place(x = 370, y = 360)

label11 = Label(root, text = "COUNTRY", bg = "Purple", fg = "White")
label11.place(x = 10, y = 390)

entry11 = Entry(root, width = 40)
entry11.place(x = 120, y = 390)

label12 = Label(root, text = "HOBBIES", bg = "Purple", fg = "White")
label12.place(x = 10, y = 420)

h1 = IntVar()
h2 = IntVar()
h3 = IntVar()
h4 = IntVar()
h5 = IntVar()
H1 = Radiobutton(root , text = "Drawing", variable = h1, value = 5, bg = "Purple").place(x = 120, y = 420)
H2 = Radiobutton(root , text = "Singing", variable = h2, value = 1, bg = "Purple").place(x = 200, y = 420)
H3 = Radiobutton(root , text = "Dancing", variable = h3, value = 2, bg = "Purple").place(x = 280, y = 420)
H4 = Radiobutton(root , text = "Sketching", variable = h4, value = 3, bg = "Purple").place(x = 360, y = 420)
H5 = Radiobutton(root , text = "Others", variable = h5, value = 4, bg = "Purple").place(x = 440, y = 420)

H6 = Entry(root, width = 30)
H6.place(x = 510, y = 420)

label13 = Label(root, text = "QUALIFICATION", bg = "Purple", fg = "White")
label13.place(x = 10, y = 450)

label14 = Label(root, text = "S.NO", bg = "Purple", fg = "White")
label14.place(x = 120, y = 480)

label15 = Label(root, text = "EXAMINATION", bg = "Purple", fg = "White")
label15.place(x = 200, y = 480)

label16 = Label(root, text = "BOARD", bg = "Purple", fg = "White")
label16.place(x = 340, y = 480)

label17 = Label(root, text = "PERCENTAGE", bg = "Purple", fg = "White")
label17.place(x = 440, y = 480)

label18 = Label(root, text = "YEAR OF PASSING", bg = "Purple", fg = "White")
label18.place(x = 560, y = 480)

label19 = Label(root, text = "1", bg = "Purple", fg = "White")
label19.place(x = 120, y = 500)

label19_1 = Label(root, text = "Class X", bg = "Purple", fg = "White")
label19_1.place(x = 200, y = 500)

entry19 = Entry(root, width = 10)
entry19.place(x = 340, y = 500)

entry19_1 = Entry(root, width = 10)
entry19_1.place(x = 440, y = 500)

entry19_2 = Entry(root, width = 10)
entry19_2.place(x = 560, y = 500)

label20 = Label(root, text = "2", bg = "Purple", fg = "White")
label20.place(x = 120, y = 530)

label20_1 = Label(root, text = "Class XII", bg = "Purple", fg = "White")
label20_1.place(x = 200, y = 530)

entry20 = Entry(root, width = 10)
entry20.place(x = 340, y = 530)

entry20_1 = Entry(root, width = 10)
entry20_1.place(x = 440, y = 530)

entry20_2 = Entry(root, width = 10)
entry20_2.place(x = 560, y = 530)

label21 = Label(root, text = "3", bg = "Purple", fg = "White")
label21.place(x = 120, y = 560)

label21_1 = Label(root, text = "Graduation", bg = "Purple", fg = "White")
label21_1.place(x = 200, y = 560)

entry21 = Entry(root, width = 10)
entry21.place(x = 340, y = 560)

entry21_1 = Entry(root, width = 10)
entry21_1.place(x = 440, y = 560)

entry21_2 = Entry(root, width = 10)
entry21_2.place(x = 560, y = 560)

label22 = Label(root, text = "4", bg = "Purple", fg = "White")
label22.place(x = 120, y = 590)

label22_1 = Label(root, text = "Masters", bg = "Purple", fg = "White")
label22_1.place(x = 200, y = 590)

entry22 = Entry(root, width = 10)
entry22.place(x = 340, y = 590)

entry22_1 = Entry(root, width = 10)
entry22_1.place(x = 440, y = 590)

entry22_2 = Entry(root, width = 10)
entry22_2.place(x = 560, y = 590)

label23 = Label(root, text = "(10 char max)", bg = "Purple", fg = "White")
label23.place(x = 340, y = 610)

label24 = Label(root, text = "(upto 2 decimal)", bg = "Purple", fg = "White")
label24.place(x = 440, y = 610)

label25 = Label(root, text = "COURSES APPLIED", bg = "Purple", fg = "White")
label25.place(x = 10, y = 630)

H_1 = IntVar
CA1 = Radiobutton(root, text = "BCA", variable = H_1, value = 0, bg = "Purple", fg = "White").place(x =120, y = 630)
CA2 = Radiobutton(root, text = "B.COM", variable = H_1, value = 0, bg = "Purple", fg = "White").place(x = 200, y = 630)
CA3 = Radiobutton(root, text = "B.SC", variable = H_1, value = 0, bg = "Purple", fg = "White").place(x = 280 , y = 630)
CA4 = Radiobutton(root, text = "B.A", variable = H_1, value = 0, bg = "Purple", fg = "White").place(x = 360 , y = 630)

Button_1 = Button(root, text = "Submit", padx = 50).place(x = 800, y = 630)
Button_2 = Button(root, text = "Reset", padx = 50).place(x = 1000, y = 630)




root.mainloop()
