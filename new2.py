from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry("400x400")
root.title("Login Form")
label1=Label(root,text="Name")			
label2=Label(root,text="Password")	
entry1=Entry(root)					
entry2=Entry(root,show="*")	
label1.place(x=100,y=70)
entry1.place(x=200,y=70)
label2.place(x=100,y=130)
entry2.place(x=200,y=130)
					
def clr():
	entry1.delete(0,END)
	entry2.delete(0,END)






def login():
	if entry1.get()=="A" and entry2.get()=="P":
		root.destroy()
		dash=Tk()
		dash.title("Dashbord")
		dash.geometry("1200x800")
		label=Label(dash,text="Doctor")
		label.pack()
		label4=Label(dash,text="Name")
		label5=Label(dash,text="Qaulification")
		label6=Label(dash,text="Specialization")
		entry4=Entry(dash)
		entry5=Entry(dash)
		entry6=Entry(dash)
		label4.place(x=500,y=70)
		entry4.place(x=600,y=70)
		label5.place(x=500,y=130)
		entry5.place(x=600,y=130)
		label6.place(x=500,y=190)
		entry6.place(x=600,y=190)
		def sub():
				name=entry4.get()
				qual=entry5.get()
				spec=entry6.get()
				conn=sqlite3.connect("db1.db")
				
				with conn:
					cur=conn.cursor()
					
					cur.execute('INSERT INTO doctor(name,qual,spec) VALUES(?,?,?)',(name,qual,spec)) 
					msg=messagebox.showinfo("Submit Status","Successfull")
		def clr():
			entry4.delete(0,END)
			entry5.delete(0,END)
			entry6.delete(0,END)
		btn3=Button(dash,text="Submit",command=sub)
		btn3.place(x=530,y=250)
		btn4=Button(dash,text="clear",command=clr)
		btn4.place(x=620,y=250)
		dash.mainloop()

	else:
		msg=messagebox.showinfo("Login Status","Login Failed")


btn1=Button(root,text="Login",command=login)
btn1.place(x=160,y=180)
btn2=Button(root,text="Clear",command=clr)
btn2.place(x=250,y=180)
root.mainloop()