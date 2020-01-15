import sqlite3

conn=sqlite3.connect("db1.db")
with conn:
	cur=conn.cursor()
	cur.execute("insert into doctor(name,qual,spec) values('Kedar','BTECH','CSE')")
	print("Record Inserted")