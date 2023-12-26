from tkinter import *


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))


def button_clear():
    entry.delete(0, END)


def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, result)

    except Exception:
        entry.delete(0, END)
        entry.insert(END, "Error")
    # finally:
    #     entry.delete(0, END)
    #     entry.insert(END, result)


# Create the main base
base = Tk()
base.title("Calculator")
base.config(bg="Black")
ft = ("Arial Bold", 14)
# Create an entry widget for displaying the result
entry = Entry(base, width=32, font=ft, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, )

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

# Create buttons
row = 1
column = 0
for label in button_labels:
    button = Button(base, text=label, font=ft, fg='black', bg='grey', padx=10, pady=10, width=5)
    button.grid(row=row, column=column)
    button.config(command=lambda btn=button: button_click(btn['text']))
    column += 1
    if column > 3:
        column = 0
        row += 1

# Clear button
clear_button = Button(base, text='C', font=ft, padx=10, pady=10, width=5, command=button_clear)
clear_button.grid(row=row, column=column)

# Equal button
equal_button = Button(base, text='=', font=ft, fg='black', bg='Orange', padx=5, pady=10, width=13, command=button_equal)
equal_button.grid(row=row + 1, column=0, columnspan=2)

# Start the main loop
base.mainloop()
