from tkinter import *

base = Tk()

base.geometry('300x400')
base.title("Login ")
base.configure(bg="Light Grey")
ft = ("Arial Bold", 15)


def eventmethod1():
    pass


txt1 = Entry(base, font=ft, width=30)
txt1.grid(row=0, column=0)

b1 = Button(base, font=ft, text="1")
b1.grid(row=1, column=0)

base.mainloop()
