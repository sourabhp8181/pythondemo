from tkinter import *
root=Tk()
root.title("Login Page")
root.geometry("300x300")

def auth():
	if ent1.get()=="A" and ent2.get()=="P":

		root.destroy()
		dash=Tk()
		dash.title("Dashboard")
		dash.geometry("1200x800")

	
		label3=Label(dash,text="Doctor")
		label3.pack()
		label4=Label(dash,text="Name :")
		ent4=Entry(dash)
		ent4.place(x=100,y=80)
		
		label5=Label(dash,text="Qualification :")
		ent5=Entry(dash)
		ent5.place(x=110,y=100)
		
		label6=Label(dash,text="Specialisaton :")
		ent6=Entry(dash)
		ent6.place(x=110,y=120)
		
		
		def sub():
			print(""+ent3.get()+ent4.get()+ent5.get())
		def clr():
			ent3.delete(0,END)
			ent4.delete(0,END)
			

		btn1=Button(root,text="Submit",command=sub)
		btn1.pack()
		btn2=Button(root,text="Clear",command=clr)
		btn2.pack()








		dash.mainloop()
	else:
		print("Password doesnt match")


label1=Label(root,text="Username")
label1.place(x=10,y=20)

ent1=Entry(root)
ent1.place(x=70,y=20)

label2=Label(root,text="Password")
label2.place(x=10,y=50)

ent2=Entry(root,show="*")
ent2.place(x=70,y=50)
btn=Button(root,text="Login",command=auth)
btn.place(x=100,y=70)
root.mainloop()




root.mainloop()