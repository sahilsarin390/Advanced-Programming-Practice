from tkinter import *
from tkinter import ttk
root=Tk()
#title

#MAIN HEADING

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

inframe = Frame(my_canvas)

my_canvas.create_window((0,0),window=inframe, anchor= "nw")

root.title("REGISTRATION INFORMATION")

Label(inframe,text="REGISTRATION INFORMATION",bg="grey",fg="black",font=("Arial Bold",25)).pack(fill=X)

#Setting window size



l1=Label(inframe,text="Registration Period: (check one)",fg="black",font=("Arial Bold",15))
l1.place(x=0,y=50)

#Adding checkbutton
ch1=Checkbutton(inframe,text="One Year",fg="black",font=10)
ch1.place(x=350,y=50)

ch2=Checkbutton(inframe,text="Two Years($2 discount applies)",fg="black",font=10)
ch2.place(x=500,y=50)

ch3=Checkbutton(inframe,text="Three Years($3 discount applies)",fg="black",font=10)
ch3.place(x=850,y=50)
l2=Label(inframe,text="(not available for vehicles subject to emissions testing)",font=10)
l2.place(x=890,y=80)
l3=Label(inframe,text="Registration Type:",fg="black",font=("Arial Bold",15))
l3.place(x=0,y=120)
ch4=Checkbutton(inframe,text="Original",fg="black",font=10)
ch4.place(x=350,y=120)
ch5=Checkbutton(inframe,text="Renewal",fg="black",font=10)
ch5.place(x=510,y=120)
ch6=Checkbutton(inframe,text="Private",fg="black",font=10)
ch6.place(x=840,y=120)
ch7=Checkbutton(inframe,text="Reissue(Plates and Decals)",fg="black",font=10)
ch7.place(x=980,y=120)
Label(inframe,text="See Reissue Plates below under plate information",fg="black",font=10).place(x=990,y=150)
ch8=Checkbutton(inframe,text="Reissue(Decals Only)",fg="black",font=10)
ch8.place(x=0,y=155)
ch9=Checkbutton(inframe,text="Rental Vehicle",fg="black",font=10)
ch9.place(x=350,y=155)

ch10=Checkbutton(inframe,text="Transfer Plate Number:",fg="black",font=10)
ch10.place(x=510,y=155)
entry = Entry(inframe,width=20)
entry.place(x=760,y=165)
l4=Label(inframe,text="ENTER PLATE NUM",fg="black",font=("Arial Bold",10))
l4.place(x=760,y=185)
ch11=Checkbutton(inframe,text='For Hire(complete "For Hire Information")',fg="black",font=10)
ch11.place(x=0,y=210)
ch12=Checkbutton(inframe,text='Ridesharing(Cannot excced 16 passengers including driver)',fg="black",font=5)
ch12.place(x=510,y=210)
l5=Label(inframe,text="Seating Capacity:",fg="black",font=("Arial Bold",15))
l5.place(x=1100,y=210)
e2=Entry(inframe)
e2.place(x=1290,y=210)

ch13=Checkbutton(inframe,text='Amateur Radio Operator call letters-Specify letters:',fg="black",font=10)
ch13.place(x=0,y=250)
e3=Entry(inframe)
e3.place(x=495,y=260)
ch14=Checkbutton(inframe,text='Other:',fg="black",font=10)
ch14.place(x=805,y=250)
e4=Entry(inframe,width=15)
e4.place(x=900,y=260)
l6=Label(inframe,text="SPECIFY",fg="black",font=("Arial Bold",13))
l6.place(x=900,y=280)
#SECOND PART
l7=Label(inframe,text="OWNER INFORMATION",font=("Arial Bold",25),bg="grey",fg="black",)
#l7.pack(fill=X,anchor=CENTER)
l7.place(x=550,y=300)

l8=Label(inframe,text="OWNERS FULL NAME(last,first,mid,suffix) OR BUSINESS NAME(if owned business) ",font=("Arial Bold",10),fg="black",)
l8.place(x=0,y=350)
l9=Label(inframe,text="TELEPHONE NUMBER",font=("Arial Bold",10),fg="black",)
l9.place(x=690,y=350)
l10=Label(inframe,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("Arial Bold",10),fg="black",)
l10.place(x=1050,y=350)
e5=Entry(inframe,width=35,bd=5)
e5.place(x=0,y=370)
e6=Entry(inframe,width=35,bd=5)
e6.place(x=690,y=370)
e7=Entry(inframe,width=35,bd=5)
e7.place(x=1050,y=370)
l11=Label(inframe,text="CO-OWNERS FULL LEGAL NAME(last,first,mid,suffix)",font=("Arial Bold",10),fg="black",)
l11.place(x=0,y=400)
l12=Label(inframe,text="TELEPHONE NUMBER",font=("Arial Bold",10),fg="black",)
l12.place(x=690,y=400)
l13=Label(inframe,text="DMV CUSTOMER NUMBER/FEIN/SSN",font=("Arial Bold",10),fg="black",)
l13.place(x=1050,y=400)
e8=Entry(inframe,width=35,bd=5)
e8.place(x=0,y=420)
e9=Entry(inframe,width=35,bd=5)
e9.place(x=690,y=420)
e10=Entry(inframe,width=35,bd=5)
e10.place(x=1050,y=420)

l14=Label(inframe,text="Owners (and Lesses if applicable)Must provide their residence/home/business address where requested,this address",font=("Arial Bold",10),fg="black",)
l14.place(x=0,y=450)
l15=Label(inframe,text="can not be a P.O box.You Must complete form ISO-01 if you would like your address(es) updated",font=("Arial Bold",10),fg="black",)
l15.place(x=0,y=470)
ll6=Label(inframe,text="RESIDENCE/BUSINESS JURISDICTION",font=("Arial Bold",10),fg="black",).place(x=1050,y=450)
e11=Entry(inframe,width=35,bd=5)
e11.place(x=1050,y=470)

l17=Label(inframe,text="OWNER'S RESIDENCE/BUSINESS JURISDICTION(Apt #if applicable)",font=("Arial Bold",10),fg="black",)
l17.place(x=0,y=490)
l18=Label(inframe,text="QTY",font=("Arial Bold",10),fg="black",)
l18.place(x=600,y=490)
l19=Label(inframe,text="STATE",font=("Arial Bold",10),fg="black",)
l19.place(x=990,y=490)
l20=Label(inframe,text="ZIP CODE",font=("Arial Bold",10),fg="black",)
l20.place(x=1100,y=490)
e11=Entry(inframe,width=35,bd=5)
e11.place(x=0,y=510)
e12=Entry(inframe,width=35,bd=5)
e12.place(x=600,y=510)
e13=Entry(inframe,width=15,bd=5)
e13.place(x=990,y=510)
e14=Entry(inframe,width=15,bd=5).place(x=1100,y=510)


l21=Label(inframe,text="OWNER'S RESIDENCE/BUSINESS JURISDICTION(Apt #if applicable)",font=("Arial Bold",10),fg="black",)
l21.place(x=0,y=530)
l22=Label(inframe,text="QTY",font=("Arial Bold",10),fg="black",)
l22.place(x=600,y=530)
l23=Label(inframe,text="STATE",font=("Arial Bold",10),fg="black",)
l23.place(x=990,y=530)
l24=Label(inframe,text="ZIP CODE",font=("Arial Bold",10),fg="black",)
l24.place(x=1100,y=530)
e11=Entry(inframe,width=35,bd=5)
e11.place(x=0,y=550)
e12=Entry(inframe,width=35,bd=5)
e12.place(x=600,y=550)
e13=Entry(inframe,width=15,bd=5)
e13.place(x=990,y=550)
e14=Entry(inframe,width=15,bd=5).place(x=1100,y=550)

#SECOND PART
l25=Label(inframe,text="OWNER EMAIL ADDRESS",font=("Arial Bold",10),fg="black",)
l25.place(x=0,y=580)
l26=Label(inframe,text="CO-OWNERS EMAIL ADDRESS",font=("Arial Bold",10),fg="black",)
l26.place(x=790,y=580)
e15=Entry(inframe,width=35,bd=5)
e15.place(x=0,y=600)
e15=Entry(inframe,width=40,bd=5).place(x=790,y=600)

#THIRD PART
l27=Label(inframe,text="ADDITIONAL INFORMATION",font=("Arial Bold",22),bg="grey",fg="black",).place(x=550,y=630)
L28=Label(inframe,text="LOCALITY WHERE VEHICLE IS PRINCIPALLY CHANGED",font=("Arial Bold",10),fg="black").place(x=0,y=670)
L29=Label(inframe,text="IF NEW LOCATION ENTER THE DATE CHANGED",font=("Arial Bold",10),fg="black",).place(x=640,y=670)
L30=Label(inframe,text="Are any of the owners/lesses on active military duty or service?",font=("Arial Bold",10),fg="black",).place(x=1110,y=670)
c1 = Checkbutton(inframe,text="CITY",font=("Arial Bold",10),fg="black").place(x=0,y=690)
c2 = Checkbutton(inframe,text="COUNTRY",font=("Arial Bold",10),fg="black").place(x=55,y=690)
c3 = Checkbutton(inframe,text="TOWN OF",font=("Arial Bold",10),fg="black").place(x=140,y=690)
e16=Entry(inframe,width=30,bd=5).place(x=230,y=690)
e17=Entry(inframe,width=50,bd=5).place(x=640,y=690)
c4 = Checkbutton(inframe,text="YES",font=("Arial Bold",10),fg="black").place(x=1200,y=690)
c5 = Checkbutton(inframe,text="NO",font=("Arial Bold",10),fg="black").place(x=1255,y=690)


L31=Label(inframe,text="IF YOU WOULD LIKE YOUR REGISTRATION RENEWALS SENT TO AN ADDRESS OTHER THAN RESDIDENCE/BUSINESS ADRESS ENTER IN TBELOW? ",font=("Arial Bold",10),fg="black",).place(x=0,y=710)
L32=Label(inframe,text="REGISTRATION MAILING ADDRESS-OPTIONAL",font=("Arial Bold",10),fg="black").place(x=0,y=730)
L33=Label(inframe,text="CITY",font=("Arial Bold",10),fg="black",).place(x=600,y=730)
L34=Label(inframe,text="STATE",font=("Arial Bold",10),fg="black",).place(x=990,y=730)
L35=Label(inframe,text="PINCODE",font=("Arial Bold",10),fg="black",).place(x=1100,y=730)
e16=Entry(inframe,width=40,bd=5).place(x=0,y=750)
e17=Entry(inframe,width=40,bd=5).place(x=600,y=750)
e18=Entry(inframe,width=40,bd=5).place(x=990,y=750)
e19=Entry(inframe,width=40,bd=5).place(x=1100,y=750)


btn = Button(inframe,text="SUBMIT",font=("Arial Bold",15),fg="black",bg="red").place(x=550,y=790)

root.mainloop()
