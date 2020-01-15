import sqlite3

conn=sqlite3.connect("db1.db")
with conn:
	cur=conn.cursor()
	cur.execute("Delete from Doctor where id='4'")
	print("Record Deleted")