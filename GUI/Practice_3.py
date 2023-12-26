# import tkinter as tk
from datetime import date as dt
from tkinter import *

ft = ("Helvetica", 12)


def main_menu():
    def get_date():
        obj = dt.today()
        d = obj.day
        m = obj.month
        y = obj.year
        today_dt = str(d) + "/" + str(m) + "/" + str(y)
        return today_dt

    # Function definitions for menu options

    def issue_book_base():
        # Add your code here

        def issue_book():
            enr = entry_issue_enrollment_num.get()
            bnum = entry_issue_book_num.get()
            i_date = get_date()

            if entry_issue_enrollment_num.get() == "" and entry_issue_book_num.get() == "":
                issue_status_label.config(text="Data Not Provided!!!", fg="red", font=ft)
            else:
                fobj = open("all_issued.txt", "a")
                fobj.write(enr + "," + bnum + "," + i_date + "," + "NA" + "," + "P\n")
                fobj.close()
                issue_status_label.config(text="Book Issued Successfully", fg="green", font=ft)

        def main():
            issue.destroy()
            main_menu()

        main_base.destroy()
        issue = Tk()
        issue.title("Library Management System")
        issue.geometry("800x600")
        #
        # # Create frames
        # issue = Frame(base)
        # return_frame = Frame(base)
        #
        # # Configure frames
        # for frame in (issue, return_frame):
        #     frame.grid(row=0, column=0, sticky="nsew")
        #
        # # Create labels and entry fields for issue frame
        label_issue_enrollment_num = Label(issue, text="Enrollment Number:", font=ft)
        label_issue_enrollment_num.grid(row=0, column=0, padx=10, pady=10, )
        entry_issue_enrollment_num = Entry(issue, font=ft)
        entry_issue_enrollment_num.grid(row=0, column=1, padx=10, pady=10)

        label_issue_book_num = Label(issue, text="Book Number:", font=ft)
        label_issue_book_num.grid(row=1, column=0, padx=10, pady=10, )
        entry_issue_book_num = Entry(issue, font=ft)
        entry_issue_book_num.grid(row=1, column=1, padx=10, pady=10)

        issue_button = Button(issue, text="Issue Book", command=issue_book, font=ft, bg="#4CAF50", fg="white")
        issue_button.grid(row=2, column=0, columnspan=1, padx=10, pady=10)

        issue_status_label = Label(issue, text="", font=ft, fg="black")
        issue_status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        main_menu_button = Button(issue, text="Main Menu", command=main, font=ft, bg="#4CAF50",
                                  fg="white")
        main_menu_button.grid(row=2, column=1, columnspan=1, padx=20, pady=10)
        column1 = label_issue_book_num.grid_info()['column']
        row1 = label_issue_book_num.grid_info()['row']

        column2 = issue_status_label.grid_info()['column']
        row2 = issue_status_label.grid_info()['row']
        print(column1, row1, column2, row2)

    def return_book_base():
        # Add your code here
        main_base.destroy()
        return_ = Tk()
        return_.title("Library Management System")
        return_.geometry("500x300")

        def _check(bn, ls):
            for i in range(len(ls)):
                temp = ls[i].split(",")
                if bn == temp[1] and temp[3] == "NA":
                    temp[3] = get_date()
                    temp[4] = 'R\n'
                    return i, temp, True
            return None, None, False

        def return_book():
            bno = entry_enrollment_num.get()
            fobj = open("all_issued.txt", "r")
            book_list = fobj.readlines()
            fobj.close()
            i, ls, check = _check(bno, book_list)

            if check:
                s = ",".join(ls)
                book_list[i] = s
                fobj = open("all_issued.txt", "w")
                fobj.writelines(book_list)
                fobj.close()
                return_status_label.config(text="Book Returned Successfully", fg="green", font=ft)
            else:
                return_status_label.config(text="Book Numbered Entered Invalid", fg="red", font=ft)

        label_enrollment_num = Label(return_, text="Enter Your Book Number:", font=ft)
        label_enrollment_num.grid(row=0, column=0, padx=10, pady=10, )
        entry_enrollment_num = Entry(return_, font=ft)
        entry_enrollment_num.grid(row=0, column=1, padx=10, pady=10)

        return_button = Button(return_, text="Return Book", command=return_book, font=ft, bg="#4CAF50", fg="white")
        return_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        return_status_label = Label(return_, text="", font=ft, fg="black")
        return_status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_new_stud_base():
        main_base.destroy()
        stud = Tk()
        stud.title("Library Management System")
        stud.geometry("500x300")

        # Add your code here
        # name = input("Enter Name:")
        # cl = input("Enter Class:")
        # mno = input("Enter Your Mobile Number:")
        # prn = input("Enter Enrollment(PRN) Number:")
        def add_stud_info():
            if len(entry_prn.get() and entry_name.get() and entry_cl.get() and entry_mno.get()) == 0:
                info_status_label.config(text="Fill All the Details!!!", fg="red", font=ft)
            else:
                fobj = open('all_stud.txt', 'a')
                fobj.write(
                    entry_prn.get() + "," + entry_name.get() + "," + entry_cl.get() + "," + entry_mno.get() + "\n")
                fobj.close()
                info_status_label.config(text="Student Data Added Successfully!!", fg="green", font=ft)

        label_name = Label(stud, text="Enter Your Name:", font=ft, bg="#4CAF50", fg="white")
        label_name.grid(row=0, column=0, padx=10, pady=10, )
        entry_name = Entry(stud, font=ft)
        entry_name.grid(row=0, column=1, padx=10, pady=10)

        label_cl = Label(stud, text="Enter Your Class:", font=ft, bg="#4CAF50", fg="white")
        label_cl.grid(row=1, column=0, padx=10, pady=10, )
        entry_cl = Entry(stud, font=ft)
        entry_cl.grid(row=1, column=1, padx=10, pady=10)

        label_prn = Label(stud, text="Enter Your PRN Number:", font=ft, bg="#4CAF50", fg="white")
        label_prn.grid(row=2, column=0, padx=10, pady=10, )
        entry_prn = Entry(stud, font=ft)
        entry_prn.grid(row=2, column=1, padx=10, pady=10)

        label_mno = Label(stud, text="Enter Your Mobile Number:", font=ft, bg="#4CAF50", fg="white")
        label_mno.grid(row=3, column=0, padx=10, pady=10, )
        entry_mno = Entry(stud, font=ft)
        entry_mno.grid(row=3, column=1, padx=10, pady=10)

        return_button = Button(stud, text="Add Info", command=add_stud_info, font=ft, bg="#4CAF50", fg="white")
        return_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        info_status_label = Label(stud, text="", font=ft, fg="black")
        info_status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_new_book_base():
        # Add your code here
        # b_no = input("Enter Book Number:")
        # b_title = input("Enter Title: ")
        # b_author = input("Enter Author: ")
        # b_pub = input("Enter Publication: ")
        main_base.destroy()
        book = Tk()
        book.title("Library Management System")
        book.geometry("500x300")

        def add_book():
            fobj = open('all_books.txt', 'a')
            fobj.write(entry_num.get() + "," + entry_tt.get() + "," + entry_at.get() + "," + entry_pub.get() + "\n")
            fobj.close()

        label_num = Label(book, text="Enter Book Number:", font=ft, bg="#4CAF50", fg="white")
        label_num.grid(row=0, column=0, padx=10, pady=10, )
        entry_num = Entry(book, font=ft)
        entry_num.grid(row=0, column=1, padx=10, pady=10)

        label_tt = Label(book, text="Enter Title:", font=ft, bg="#4CAF50", fg="white")
        label_tt.grid(row=1, column=0, padx=10, pady=10, )
        entry_tt = Entry(book, font=ft)
        entry_tt.grid(row=1, column=1, padx=10, pady=10)

        label_at = Label(book, text="Enter Author:", font=ft, bg="#4CAF50", fg="white")
        label_at.grid(row=2, column=0, padx=10, pady=10, )
        entry_at = Entry(book, font=ft)
        entry_at.grid(row=2, column=1, padx=10, pady=10)

        label_pub = Label(book, text="Enter Publication:", font=ft, bg="#4CAF50", fg="white")
        label_pub.grid(row=3, column=0, padx=10, pady=10, )
        entry_pub = Entry(book, font=ft)
        entry_pub.grid(row=3, column=1, padx=10, pady=10)

        add_button = Button(book, text="Add Book", command=add_book, font=ft, bg="#4CAF50", fg="white")
        add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        info_status_label = Label(book, text="", font=ft, fg="black")
        info_status_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def show_not_ret_books_base():
        # Add your code here
        pass

    def stud_history_base():
        # Add your code here
        def stud_history():
            prn = entry_prn.get()
            entry_prn.delete(0, END)
            fobj = open("all_issued.txt", "r")
            ls = fobj.readlines()
            fobj.close()
            check = False
            s = ""
            for i in range(len(ls)):
                temp = ls[i].split(",")
                if prn == temp[0]:
                    # print(temp[1], temp[2], temp[3], sep="\t\t")
                    s = temp[1] + "\t" + temp[2] + "\t" + temp[3]
                    check = True
                    break

            if check:
                result_label.config(text=s, font=("Times New Roman", 12), fg="Grey")
            else:
                result_label.config(text="No Such Record Found ", font=("Times New Roman", 12), fg="Red")

        main_base.destroy()
        stud = Tk()
        stud.title("Library Management System")
        stud.geometry("500x300")

        label_prn = Label(stud, text="Enter Your PRN Number:", font=ft, bg="#4CAF50", fg="white")
        label_prn.grid(row=1, column=0, padx=10, pady=10, )
        entry_prn = Entry(stud, font=ft)
        entry_prn.grid(row=1, column=1, padx=10, pady=10)

        get_info = Button(stud, text="Get Info", font=ft, bg="#4CAF50", fg="white", command=stud_history)
        get_info.grid(row=2, column=0, columnspan=2)

        result_label = Label(stud, text="", )
        result_label.grid(row=3, column=0, columnspan=3)

    def book_history_base():
        # Add your code here
        pass

    def search_book_base():
        # Add your code here
        pass

    def search_stud_base():
        # Add your code here
        pass

        # Create main base

    main_base = Tk()
    main_base.title("Library Management System")
    main_base.geometry("800x600")

    # Create main menu frame
    main_frame = Frame()
    main_frame.grid(column=0)

    # Create labels and buttons for main menu frame
    label_main_menu = Label(main_frame, text="Main Menu", font=("Times New Roman", 20))

    label_main_menu.grid(column=0)

    button_issue_book = Button(main_frame, text="Issue Book", command=issue_book_base, font=ft, bg="#4CAF50",
                               fg="white")
    button_issue_book.grid(column=0)

    button_return_book = Button(main_frame, text="Return Book", command=return_book_base, font=ft,
                                bg="#4CAF50", fg="white")
    button_return_book.grid(column=0)

    button_add_new_stud = Button(main_frame, text="Add New Student", command=add_new_stud_base, font=ft,
                                 bg="#4CAF50", fg="white")
    button_add_new_stud.grid(column=0)

    button_add_new_book = Button(main_frame, text="Add New Book", command=add_new_book_base, font=ft,
                                 bg="#4CAF50", fg="white")
    button_add_new_book.grid(column=0)

    button_show_not_ret_books = Button(main_frame, text="Show Not Returned Books", command=show_not_ret_books_base,
                                       font=ft, bg="#4CAF50", fg="white")
    button_show_not_ret_books.grid(column=0)

    button_stud_history = Button(main_frame, text="Student History", command=stud_history_base, font=ft,
                                 bg="#4CAF50", fg="white")
    button_stud_history.grid(column=0)

    button_book_history = Button(main_frame, text="Book History", command=book_history_base, font=ft,
                                 bg="#4CAF50", fg="white")
    button_book_history.grid(column=0)

    button_search_book = Button(main_frame, text="Search Book", command=search_book_base, font=ft,
                                bg="#4CAF50", fg="white")
    button_search_book.grid(column=0)

    button_search_stud = Button(main_frame, text="Search Student", command=search_stud_base, font=ft,
                                bg="#4CAF50", fg="white")
    button_search_stud.grid(column=0)

    button_exit = Button(main_frame, text="Exit", command=main_base.destroy, font=ft, bg="#4CAF50", fg="white")
    button_exit.grid(column=0, padx=20,pady=10, ipadx=20,sticky="w")

    # Run the main event loop
    main_base.mainloop()


main_menu()
