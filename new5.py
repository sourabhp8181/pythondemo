from tkinter import ttk
from tkinter import *
import sqlite3

root=Tk()
root.geometry("1200x800")
root.title("INFO")
treeV=ttk.Treeview(root,column=('One','Two','Three'),selectmode="extended")
treeV.heading('#0',text="id",anchor=CENTER)
treeV.heading('#1',text="name",anchor=CENTER)
treeV.heading('#2',text="qual",anchor=CENTER)
treeV.heading('#3',text="spec",anchor=CENTER)
treeV.column('#0',minwidth=20,width=30,stretch=YES)
treeV.column('#1',minwidth=50,width=100,stretch=YES)
treeV.column('#2',minwidth=50,width=100,stretch=YES)
treeV.column('#3',minwidth=50,width=100,stretch=YES)
treeV.pack()

conn=sqlite3.connect("db1.db")
with conn:
	cur=conn.cursor()
	cur.execute("Select * FROM Doctor ORDER BY id DESC")
for row in cur.fetchall():
	treeV.insert('', 0, text=row[0],values=(row[1],row[2],row[3]))

root.mainloop()