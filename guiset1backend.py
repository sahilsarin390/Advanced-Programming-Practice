import sqlite3

conn = sqlite3.connect('')
 
cursor = conn.cursor()


cursor.execute("""CREATE TABLE form(
	e1.text 
	e2.text 
	e4.text 
	e5.integer 
	e6.text 
	e7.text 
	e8.integer 
	e9.text 
	e10.text
	e11.text
	e12.text
	e13.text
	e14.text
	e15.text
	e16.text
	e17.text
	e18.text
	e19.integer
	e20.integer
	e21.integer
	e22.integer
	e23.text
	)""")

conn.commit()

conn.close()



    print ('Your Registration is Successfull!!')