# from base import *
#
# base = Tk()
#
# base.geometry('300x400')
# base.title("Calculator")
# base.configure(bg="LightGrey")
# ft = ("Arial Bold", 12)
#
#
# base.mainloop()


# import base as tk
#
# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(number))
#
# def button_clear():
#     entry.delete(0, tk.END)
#
# def button_equal():
#     expression = entry.get()
#     try:
#         result = eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, result)
#     except Exception:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")
#
# # Create the main window
# window = tk.Tk()
# window.geometry("300x400")
# window.title("Calculator")
#
# # Create an entry widget for displaying the result
# entry = tk.Entry(window, width=30, borderwidth=5)
# entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
# # Define buttons
# buttons = \
#     [
#     ('7', 1, 0),
#     ('8', 1, 1),
#     ('9', 1, 2),
#     ('4', 2, 0),
#     ('5', 2, 1),
#     ('6', 2, 2),
#     ('1', 3, 0),
#     ('2', 3, 1),
#     ('3', 3, 2),
#     ('0', 4, 0),
#     ('+', 1, 3),
#     ('-', 2, 3),
#     ('*', 3, 3),
#     ('/', 4, 3),
#     ('C', 4, 1),
#     ('=', 4, 2)
# ]
#
# # Create buttons
# for button_text, row, column in buttons:
#     button = tk.Button(window, text=button_text, padx=20, pady=20, command=lambda text=button_text: button_click(text))
#     button.grid(row=row, column=column)
#
# # Clear button
# clear_button = tk.Button(window, text='Clear', padx=20, pady=20, command=button_clear)
# clear_button.grid(row=3, column=0)
#
# # Equal button
# equal_button = tk.Button(window, text='=', padx=20, pady=20, command=button_equal)
# equal_button.grid(row=3, column=2)
#
# # Start the main loop
# window.mainloop()


# import base as tk
#
# def button_click(number):
#     current = entry.get()
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, current + str(number))
#
# def button_clear():
#     entry.delete(0, tk.END)
#
# def button_equal():
#     expression = entry.get()
#     try:
#         result = eval(expression)
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, result)
#     except Exception:
#         entry.delete(0, tk.END)
#         entry.insert(tk.END, "Error")
#
# # Create the main window
# window = tk.Tk()
# window.title("Calculator")
#
# # Create an entry widget for displaying the result
# entry = tk.Entry(window, width=20, justify=tk.RIGHT)
# entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
#
# # Define button labels
# button_labels = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]
#
# # Create buttons
# row = 1
# column = 0
# for label in button_labels:
#     button = tk.Button(window, text=label, padx=10, pady=10, width=5, command=lambda text=label: button_click(text))
#     button.grid(row=row, column=column)
#     column += 1
#     if column > 3:
#         column = 0
#         row += 1
#
# # Clear button
# clear_button = tk.Button(window, text='C', padx=10, pady=10, width=5, command=button_clear)
# clear_button.grid(row=row, column=column)
#
# # Equal button
# equal_button = tk.Button(window, text='=', padx=10, pady=10, width=5, command=button_equal)
# equal_button.grid(row=row, column=3, columnspan=2)
#
# # Start the main loop
# window.mainloop()


from tkinter import *


class Expression:
    expression = ""

    @classmethod
    def set(cls, expression):
        cls.expression = expression
        return cls.expression

    @classmethod
    def get(cls):
        return cls.expression


def on_button_press(equation, value):
    Expression.set(Expression.get() + str(value))
    equation.set(Expression.get())


def on_equal_button_press(equation):
    try:
        total = str(eval(Expression.get()))
        equation.set(total)
    except:
        equation.set(" error ")
    finally:
        Expression.set("")


def on_clear_button_press(equation):
    Expression.set("")
    equation.set("")


def create_window(base):
    base.configure(bg="Light Grey")
    base.title("Simple Calculator")
    base.geometry("300x400")

    return base


def add_buttons(base, equation):
    add_button(base, ' 1 ', lambda: on_button_press(equation, '1'), 2, 0)
    add_button(base, ' 2 ', lambda: on_button_press(equation, '2'), 2, 1)
    add_button(base, ' 3 ', lambda: on_button_press(equation, '3'), 2, 2)
    add_button(base, ' 4 ', lambda: on_button_press(equation, '4'), 3, 0)
    add_button(base, ' 5 ', lambda: on_button_press(equation, '5'), 3, 1)
    add_button(base, ' 6 ', lambda: on_button_press(equation, '6'), 3, 2)
    add_button(base, ' 7 ', lambda: on_button_press(equation, '7'), 4, 0)
    add_button(base, ' 8 ', lambda: on_button_press(equation, '8'), 4, 1)
    add_button(base, ' 9 ', lambda: on_button_press(equation, '9'), 4, 2)
    add_button(base, ' 0 ', lambda: on_button_press(equation, '0'), 5, 0)
    add_button(base, ' + ', lambda: on_button_press(equation, '+'), 2, 3)
    add_button(base, ' - ', lambda: on_button_press(equation, '-'), 3, 3)
    add_button(base, ' * ', lambda: on_button_press(equation, '*'), 4, 3)
    add_button(base, ' / ', lambda: on_button_press(equation, '/'), 5, 3)
    add_button(base, ' = ', lambda: on_equal_button_press(equation), 5, 2)
    add_button(base, ' Clear ', lambda: on_clear_button_press(equation), 5, 1)


def add_button(base, text, command, row, column):
    button = Button(base, text=text, fg='black', bg='Light Blue', command=command, height=2, width=8)
    button.grid(row=row, column=column)


def add_textbox(base):
    equation = StringVar()
    expression_field = Entry(base, font=("Arial Bold", 15), textvariable=equation)
    expression_field.grid(columnspan=6, pady=(0, 3), ipadx=65)

    return equation


base = Tk()

base = create_window(base)
equation = add_textbox(base)
add_buttons(base, equation)
base.mainloop()
