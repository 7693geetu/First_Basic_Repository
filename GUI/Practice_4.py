
from tkinter import *

base = Tk()
base.geometry("300x300")
base.title("Demonstrating Menu")


def add():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    e3.insert(0, str(a + b), )


def sub():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    e3.insert(0, str(a - b), )


def mul():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    e3.insert(0, str(a * b), )


def div():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    e3.insert(0, str(a / b), )


def check_greater():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    if a > b:
        s = str(a) + " is Greater Than " + str(b)
        e3.insert(0, s, )
    elif b > a:
        s = str(b) + " is Greater Than " + str(a)
        e3.insert(0, s, )


def check_lesser():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    if a < b:
        s = str(a) + " is Less Than " + str(b)
        e3.insert(0, s, )
    elif b < a:
        s = str(b) + " is Less Than " + str(a)
        e3.insert(0, s, )


def check_equal():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    if a == b:
        s = str(a) + " is Equal To" + str(b)
        e3.insert(0, s, )


def check_not_equal():
    e3.delete(0, END)
    a = int(e1.get())
    b = int(e2.get())
    if a != b:
        s = str(a) + " is Not Equal To" + str(b)
        e3.insert(0, s, )


l1 = Label(base, text="Operand 1:")
l1.grid(row=1, column=1)
l2 = Label(base, text="Operand 2:")
l2.grid(row=2, column=1)
l3 = Label(base, text="Result :")
l3.grid(row=3, column=1)

e1 = Entry(base, width=20)
e1.grid(row=1, column=2)
e2 = Entry(base, width=20)
e2.grid(row=2, column=2)
e3 = Entry(base, width=20)
e3.grid(row=3, column=2)

mb = Menu(base)

m1 = Menu(mb, tearoff=0)  # <--- creating first menu
m1.add_command(label="Addition", command=add)
# adding menuitems under first menu
m1.add_command(label="Subtraction", command=sub)
m1.add_separator()
# adding separator
m1.add_command(label="Multiplication", command=mul)
m1.add_command(label="Division", command=div)
m1.add_separator()
m1.add_command(label="Exit", command=exit)

m2 = Menu(mb, tearoff=0)  # <--- creating second menu
m2.add_command(label="Check Greater Than", command=check_greater)
# adding menuitems under second menu
m2.add_command(label="Check Less Than", command=check_lesser)
m2.add_separator()
m2.add_command(label="Check Equal", command=check_equal)
m2.add_command(label="Check Not Equal", command=check_not_equal)

mb.add_cascade(label="Arithmetic Operation", menu=m1)
# adding first menu under menubar
mb.add_cascade(label="Relational Operation", menu=m2)
# adding second menu under menubar


# adding third menu under menubar

base.configure(menu=mb)
# configuring menubar to place at its standard place
base.mainloop()
