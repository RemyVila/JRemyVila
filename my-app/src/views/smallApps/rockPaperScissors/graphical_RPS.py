import tkinter as tk
import random

# Initial session stats
wins = 0
losses = 0
draws = 0
times_played = 0

def play_game(choice):
    global wins, losses, draws, times_played

    robo_choice = random.randint(1, 3)
    user_choice = choice

    result_text = ""

    if user_choice == robo_choice:
        draws += 1
        result_text = "It's a draw!"
    elif (user_choice == 1 and robo_choice == 3) or (user_choice == 2 and robo_choice == 1) or (user_choice == 3 and robo_choice == 2):
        wins += 1
        result_text = "You won!"
    else:
        losses += 1
        result_text = "You lost!"

    times_played += 1

    result_label.config(text=result_text)
    stats_label.config(text=f"Wins: {wins}, Losses: {losses}, Draws: {draws}, Times Played: {times_played}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Create GUI components
label = tk.Label(root, text="Press a button to play:")
label.pack()

rock_button = tk.Button(root, text="Rock", command=lambda: play_game(1))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game(2))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game(3))
scissors_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

stats_label = tk.Label(root, text="")
stats_label.pack()

# Start the GUI main loop
root.mainloop()