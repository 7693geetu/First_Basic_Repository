import tkinter as tk
from tkinter import messagebox


def start_game():
    """Starts a new game."""
    global current_player, board

    current_player = "X"
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Close the current window and create a new instance
    root.destroy()
    create_window()


def make_move(row, col):
    """Makes a move in the game and updates the GUI."""
    global current_player

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state="disabled")

        # Check if there's a winner
        winner = check_winner(board)
        if winner:
            disable_board()
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
        else:
            # Check for a tie
            if all(board[row][col] != " " for row in range(3) for col in range(3)):
                disable_board()
                messagebox.showinfo("Game Over", "It's a tie!")

        # Switch player
        current_player = "O" if current_player == "X" else "X"
        status_label.config(text=f"Player {current_player}'s turn")


def check_winner(board):
    """Checks if there's a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # No winner
    return None
def reset_board():
    """Resets the board and enables all the buttons."""
    global current_player, board

    current_player = "X"
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    for row in buttons:
        for button in row:
            button.config(text=" ", state="normal")

    status_label.config(text=f"Player {current_player}'s turn")

def disable_board():
    """Disables all the buttons on the board."""
    for row in buttons:
        for button in row:
            button.config(state="disabled")

def entry_window():
    pass
def create_window():
    """Creates the main window."""
    global root, buttons, status_label

    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = []
    for row in range(3):
        button_row = []
        for col in range(3):
            button = tk.Button(root, text=" ", font=("Helvetica", 32), width=3, height=1,
                               command=lambda row=row, col=col: make_move(row, col))
            button.grid(row=row, column=col, sticky="nsew")
            button_row.append(button)
        buttons.append(button_row)

    status_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 16))
    status_label.grid(row=3, column=0, columnspan=3)

    restart_button = tk.Button(root, text="Restart", font=("Helvetica", 16), command=start_game)
    restart_button.grid(row=4, column=0, columnspan=2, sticky="nsew")

    reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=reset_board)
    reset_button.grid(row=4, column=2, columnspan=2, sticky="nsew")


# Start the game
current_player = "X"
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
create_window()
root.mainloop()
# import tkinter as tk
# from tkinter import messagebox
#
# current_player = "X"
# board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
#
# def make_move(row, col):
#     """Makes a move in the game and updates the GUI."""
#     global current_player
#
#     if board[row][col] == " ":
#         board[row][col] = current_player
#         buttons[row][col].config(text=current_player, state="disabled")
#
#         # Check if there's a winner
#         winner = check_winner(board)
#         if winner:
#             disable_board()
#             messagebox.showinfo("Game Over", f"Player {winner} wins!")
#         else:
#             # Check for a tie
#             if all(board[row][col] != " " for row in range(3) for col in range(3)):
#                 disable_board()
#                 messagebox.showinfo("Game Over", "It's a tie!")
#
#         # Switch player
#         current_player = "O" if current_player == "X" else "X"
#         status_label.config(text=f"Player {current_player}'s turn")
#
# def check_winner(board):
#     """Checks if there's a winner."""
#     # Check rows
#     for row in board:
#         if row[0] == row[1] == row[2] != " ":
#             return row[0]
#
#     # Check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] != " ":
#             return board[0][col]
#
#     # Check diagonals
#     if board[0][0] == board[1][1] == board[2][2] != " ":
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != " ":
#         return board[0][2]
#
#     # No winner
#     return None
#
# def disable_board():
#     """Disables all the buttons on the board."""
#     for row in buttons:
#         for button in row:
#             button.config(state="disabled")
#

#
# def restart_game():
#     """Restarts the game by resetting the board and enabling all the buttons."""
#     reset_board()
#     enable_board()
#
# def enable_board():
#     """Enables all the buttons on the board."""
#     for row in buttons:
#         for button in row:
#             button.config(state="normal")
#
# # Create the main window
# root = tk.Tk()
# root.title("Tic-Tac-Toe")
#
# # Create the game board
# buttons = []
# for row in range(3):
#     button_row = []
#     for col in range(3):
#         button = tk.Button(root, text=" ", font=("Helvetica", 32), width=3, height=1,
#                            command=lambda row=row, col=col: make_move(row, col))
#         button.grid(row=row, column=col, sticky="nsew")
#         button_row.append(button)
#     buttons.append(button_row)
#
# # Create the status label
# status_label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Helvetica", 16))
# status_label.grid(row=3, column=0, columnspan=3)
#
# # Create the reset button
# reset_button = tk.Button(root, text="Reset", font=("Helvetica", 16), command=reset_board)
# reset_button.grid(row=4, column=0, sticky="nsew")
#
# # Create the restart button
# restart_button = tk.Button(root, text="Restart", font=("Helvetica", 16), command=restart_game)
# restart_button.grid(row=4, column=1, columnspan=2, sticky="nsew")
#
# # Start the game
# root.mainloop()
