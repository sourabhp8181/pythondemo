from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("RadioButton")
root.geometry("400x400")
rbstr=StringVar()
def disp():
	print("You Selected "+rbstr.get())
rb1=Radiobutton(root,text="Male",variable=rbstr,value="Male",command=disp)
rb2=Radiobutton(root,text="Female",variable=rbstr,value="Female",command=disp)
rb1.pack()
rb2.pack()
root.mainloop()

