from tkinter import *

def main_menu_frame():
    base = Tk()
    base.geometry("400x200")
    base.title("Main Menu")
    base.configure(bg="yellow")
    ft = ("Arial Bold", 13)

    def eventmethod1(event_metadata):
        base.destroy()
        issue_book_frame()

    lb1 = Label(base, text="This is Main Menu", font=ft)
    lb1.pack()

    lb2 = Label(base, text="Issue Book", font=ft)
    lb2.bind("<Button-1>", eventmethod1)
    lb2.pack()

    base.mainloop()

def issue_book_frame():
    base = Tk()
    base.geometry("500x500")
    base.title("Issue Book Form")
    ft = ("Comic Sans MS", 13)

    def eventmethod2():
        exit(0)

    btn = Button(base, text="Exit", font=ft)
    btn.configure(command=eventmethod2)
    btn.pack()

    base.mainloop()

# open area begins from here
main_menu_frame()