from tkinter import *

parent=Tk()

parent.geometry('250x150')

salary = IntVar()
salary.set("")
amount = IntVar()
amount.set("")

def daily(salary):
    d= salary/30
    amount.set(d)

def weekly(salary):
    d= (salary/30)*7
    amount.set(d)

l1 = Label(parent,text="Amount").place(x=20,y=110)
show = Entry(parent,text=amount).place(x=70,y=110)

l2 = Label(parent,text="Salary").place(x=20,y=20)
getsalary = Entry(parent,text=salary).place(x=70,y=20)

button1 = Button(parent,text="Daily",command=lambda:daily(salary.get())).place(x=60,y=60)
button2 = Button(parent,text="Weekly",command=lambda:weekly(salary.get())).place(x=120,y=60)


parent.mainloop()