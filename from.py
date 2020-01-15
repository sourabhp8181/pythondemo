from tkinter import *
root=Tk()
root.title("Login Form")
root.geometry("400x400")

label1=Label(root,text="Username")
label1.place(x=10,y=20)

ent1=Entry(root)
ent1.place(x=70,y=20)

label2=Label(root,text="Password")
label2.place(x=10,y=50)

ent2=Entry(root,show="*")
ent2.place(x=70,y=50)
root.mainloop()

