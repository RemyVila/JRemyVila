import random

# Initial session stats
wins = 0
losses = 0
draws = 0
times_played = 0

print("Press Enter if you'd like to play Rock, Paper, Scissors.")

# MEAT OF THE GAME
def rock_paper_scissors():
    global wins, losses, draws, times_played

    robo_choice = random.randint(1, 3)
    user_choice = None

    while user_choice not in {'1', '2', '3'}:
        user_choice = input("Choose 1 for Rock, 2 for Paper, 3 for Scissors: ")

    user_choice = int(user_choice)

    if user_choice == 1:
        if robo_choice == 1:
            draws += 1
            print("We both chose Rock. It's a draw.")
        elif robo_choice == 2:
            losses += 1
            print("You chose Rock, I chose Paper. You lost. Get rekt noob.")
        elif robo_choice == 3:
            wins += 1
            print("You chose Rock, I chose Scissors. You won :/")
    elif user_choice == 2:
        if robo_choice == 1:
            wins += 1
            print("You chose Paper, I chose Rock. You won :/")
        elif robo_choice == 2:
            draws += 1
            print("We both chose Paper. It's a draw.")
        elif robo_choice == 3:
            losses += 1
            print("You chose Paper, I chose Scissors. I won. Get rekt noob.")
    elif user_choice == 3:
        if robo_choice == 1:
            losses += 1
            print("You chose Scissors, I chose Rock. I won. Get rekt noob.")
        elif robo_choice == 2:
            wins += 1
            print("You chose Scissors, I chose Paper. You won :/")
        elif robo_choice == 3:
            draws += 1
            print("We both chose Scissors. It's a draw.")

    times_played += 1

# PRESS ENTER TO START NEW GAME
def new_game():
    global wins, losses, draws, times_played

    input("Press Enter to start a new game.")
    rock_paper_scissors()

    print("Wins:", wins)
    print("Losses:", losses)
    print("Draws:", draws)
    print("Times played:", times_played)

# PRESS ENTER TO START FIRST GAME
while True:
    new_game()
