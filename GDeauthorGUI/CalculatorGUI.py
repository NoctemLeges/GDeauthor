from tkinter import *


arg1=0
global flag

root = Tk()
root.title("Calculator")

e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)


def buttonClick(number):
    residue = e.get()
    e.delete(0,END)
    e.insert(0,str(residue)+str(number))

def clearInput():
    e.delete(0,END)

def add():
   global arg1
   global flag
   arg1 = int(e.get())
   flag = 0
   e.delete(0,END)

def sub():
   global arg1
   global flag
   arg1 = int(e.get())
   flag = 1
   e.delete(0,END)

def mul():
   global arg1
   global flag
   arg1 = int(e.get())
   flag = 2
   e.delete(0,END)

def div():
   global arg1
   global flag
   arg1 = int(e.get())
   flag = 3
   e.delete(0,END)

def result():
    global arg1
    global flag
    arg2 = int(e.get())
    e.delete(0,END)
    if flag==0:
        e.insert(0,arg1+arg2)
    if flag==1:
        e.insert(0,arg1-arg2)
    if flag==2:
        e.insert(0,arg1*arg2)
    if flag==3:
        e.insert(0,arg1//arg2)


button1=Button(root,text="1",padx=55,pady=20,command=lambda: buttonClick(1))
button2=Button(root,text="2",padx=55,pady=20,command=lambda: buttonClick(2))
button3=Button(root,text="3",padx=55,pady=20,command=lambda: buttonClick(3))
button4=Button(root,text="4",padx=55,pady=20,command=lambda: buttonClick(4))
button5=Button(root,text="5",padx=55,pady=20,command=lambda: buttonClick(5))
button6=Button(root,text="6",padx=55,pady=20,command=lambda: buttonClick(6))
button7=Button(root,text="7",padx=55,pady=20,command=lambda: buttonClick(7))
button8=Button(root,text="8",padx=55,pady=20,command=lambda: buttonClick(8))
button9=Button(root,text="9",padx=55,pady=20,command=lambda: buttonClick(9))
button0=Button(root,text="0",padx=55,pady=20,command=lambda: buttonClick(0))
button_add = Button(root,text="+",padx=115,pady=20,command=add)
button_sub = Button(root,text="-",padx=55,pady=20,command=sub)
button_mul = Button(root,text="*",padx=55,pady=20,command=mul)
button_div = Button(root,text="/",padx=55,pady=20,command=div)
button_equals = Button(root,text="=",padx=53,pady=52,command=result)
button_clear = Button(root,text = "CLEAR",padx=38,pady=20,command=clearInput)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

button_add.grid(row=5,column=0,columnspan=2)
button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)

button_clear.grid(row=4,column=1)
button_equals.grid(row=4,column=2,rowspan=2)

root.mainloop()
