import sqlite3

conn=sqlite3.connect("db1.db")
with conn:
	cur=conn.cursor()
	cur.execute("UPDATE Doctor set name='Kedar Habibi' where id='4'")
	print("Record Updated")