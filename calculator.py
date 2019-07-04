from tkinter import * 
import getpass

t=Tk()

# by using grid
# l_name = Label(t,text="Name").grid(row="0",column="0")
# name = Entry(t).grid(row="0",column="1")
# l_password = Label(t,text="Password").grid(row="1",column="0")
# password = Entry(t,show="*").grid(row="1",column="1")
# button = Button(t,text="submit").grid(row="4",column="1")

t.geometry("250x150")
# l_name = Label(t,text="Name").place(x=30,y=50)
# name = Entry(t).place(x=80,y=50)
# l_password = Label(t,text="Password").place(x=30,y=70)
# password = Entry(t,show="*").place(x=90,y=70)
# button = Button(t,text="submit").place(x=30,y=50)

n1 = IntVar()
n1.set("")
n2 = IntVar()
n2.set("")
n3 = IntVar()
n3.set("")

def add(n1,n2):
    add= n1+n2
    n3.set(add)

number1= Label(t,text="Number 1").grid(row=0)
e1= Entry(t,text=n1).grid(row=0,column=1)
number2= Label(t,text="Number 2").grid(row=1)
e2= Entry(t,text=n2).grid(row=1,column=1)
number3= Label(t,text="Result").grid(row=2)
e3= Entry(t,text=n3).grid(row=2,column=1)
button = Button(t,text="submit",command=lambda:add(n1.get(),n2.get())).grid(row=3,column=1)

t.mainloop()