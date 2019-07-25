from tkinter import *

top=Tk()
top.geometry("400x250")  
n1=IntVar()
n1.set("")

n2=IntVar()
n2.set("")

n3=IntVar()
n3.set("")

def add(n1,n2):
    add=n1+n2
    n3.set(add)

number1=Label(top,text="number 1")
number1.grid()

number2=Label(top,text="number 2")
number2.grid(row=1)

result=Label(top,text="Result")
result.grid(row=2)

e1=Entry(top,textvariable=n1)
e1.grid(row=0,column=1)

e2=Entry(top,textvariable=n2)
e2.grid(row=1,column=1)

e3=Entry(top,text=n3)
e3.grid(row=2,column=1)

submit=Button(top,text="Add",command=lambda:add(n1.get(),n2.get()))
submit.grid(row=3)
top.mainloop()
