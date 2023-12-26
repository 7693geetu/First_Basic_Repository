from tkinter import *
import random


def start_game(x, y):
    root.destroy()
    ft = ('consolas', 40)

    players = ["x", "o"]
    names = [x, y]
    player = random.choice(players)
    buttons = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    def next_turn(row, column):
        nonlocal player

        if buttons[row][column]['text'] == "" and check_winner() is False:

            if player == players[0]:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[1]
                    label.config(text=(names[1] + " -> turn"))

                elif check_winner() is True:
                    label.config(text=(names[0] + "-> Wins"))

                elif check_winner() == "Tie":
                    label.config(text="Its a Tie!")

            else:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[0]
                    label.config(text=(names[0] + "-> turn"))

                elif check_winner() is True:
                    label.config(text=(names[1] + "-> Wins"))

                elif check_winner() == "Tie":
                    label.config(text="Its a Tie!")

    def check_winner():
        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                buttons[row][0].config(bg="green")
                buttons[row][1].config(bg="green")
                buttons[row][2].config(bg="green")
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                buttons[0][column].config(bg="green")
                buttons[1][column].config(bg="green")
                buttons[2][column].config(bg="green")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][0].config(bg="green")
            return True

        elif empty_spaces() is False:
            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="Red")
            return "Tie"

        else:
            return False

    def empty_spaces():
        spaces = 9

        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game():
        nonlocal player

        player = random.choice(players)

        label.config(text=names[players.index(player)] + " -> Turn")

        for r in range(3):
            for c in range(3):
                buttons[r][c].config(text="", bg="#F0F0F0")

    window = Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("500x500")
    window.config(bg="#333333")

    label = Label(text=names[players.index(player)]+ " -> Turn", font=ft)
    label.grid(row=0,columnspan=2)

    reset_button = Button(text="Reset", font=('consolas', 20), command=new_game, bg="orange")
    reset_button.grid(row=1,column=0)


    frame = Frame(window)
    frame.grid(row=3)

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", font=ft, width=3, height=1,
                                          command=lambda row=row, column=column: next_turn(row, column))
            buttons[row][column].grid(row=row, column=column)

    window.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")
    ft = ("times new roman", 15)
    l1 = Label(root, text="Enter Player 1", font=ft)
    l1.grid(row=1, column=1, pady=10)
    e1 = Entry(root, font=ft)
    e1.grid(row=1, column=2, pady=10)

    l2 = Label(root, text="Enter Player 2", font=ft)
    l2.grid(row=2, column=1, pady=10)
    e2 = Entry(root, font=ft)
    e2.grid(row=2, column=2, pady=10)


    def check_start():
        if len(e1.get() and e2.get()) == 0:
            l = Label(root, text="Fill the Names Properly!!!", font=ft, fg="Red")
            l.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        else:
            start_game(e1.get(), e2.get())


    b = Button(text="Start The Game", font=ft, command=check_start, activebackground="green", bg="skyblue")
    b.grid(row=3, column=1, columnspan=2, pady=10)
    root.mainloop()
