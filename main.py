import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors Game")
        self.master.configure(bg='lightblue')
        self.master.geometry("1100x600")  # Increase the window size

        self.label = tk.Label(master, text="CHOOSE ROCK, PAPER, OR  SCISSORS:", bg='lightblue', font=('C', 22))
        self.label.grid(row=0, column=0, columnspan=3, pady=20)

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play("Rock"), bg='lightcoral', font=('Arial', 12), width=35)
        self.rock_button.grid(row=1, column=0, padx=20, pady=10)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play("Paper"), bg='lightgreen', font=('Arial', 12), width=35)
        self.paper_button.grid(row=1, column=1, padx=20, pady=10)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play("Scissors"), bg='lightyellow', font=('Arial', 12), width=35)
        self.scissors_button.grid(row=1, column=2, padx=20, pady=10)

        self.result_label = tk.Label(master, text="", bg='lightblue', font=('Arial', 12))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=20)

    def play(self, player_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        result = self.determine_winner(player_choice, computer_choice)

        result_text = f"Player chose: {player_choice}\nComputer chose: {computer_choice}\nResult: {result}"
        self.result_label.config(text=result_text)

        if result == "Player wins!":
            messagebox.showinfo("Game Result", "Congratulations! You win!")
        elif result == "Computer wins!":
            messagebox.showinfo("Game Result", "Sorry, you lost. Computer wins!")
        else:
            messagebox.showinfo("Game Result", "It's a tie!")

    def determine_winner(self, player, computer):
        if computer == player:
            return "It's a tie!"
        elif (player == "Rock" and computer == "Scissors") or \
             (player == "Paper" and computer == "Rock") or \
             (player == "Scissors" and computer == "Paper"):
            return "Player wins!"
        else:
            return "player wins!"

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
