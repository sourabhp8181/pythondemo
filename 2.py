from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("RadioButton")
root.geometry("400x400")
rbstr=StringVar()
def disp():
	lb1=Label(root,text=rbstr.get()).place(x=40,y=50)
	
rb1=Radiobutton(root,text="Male",variable=rbstr,value="Male")
rb2=Radiobutton(root,text="Female",variable=rbstr,value="Female")
btn1 =  Button(root,text="Click me",command=disp)
btn1.pack()
rb1.pack()
rb2.pack()
root.mainloop()

