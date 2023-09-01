import json
import random
import tkinter as tk
from tkinter import messagebox

def hangman_game():
    # Open and read the JSON file
    with open("wBank.json", "r") as file:
        wBank = json.load(file)

    def guess_letter(guess, letters_list, letters_known, limbs):
        guess = guess.lower()  # Convert guess to lowercase
        if guess in letters_list:
            for i in range(len(letters_list)):
                if letters_list[i] == guess:
                    letters_known[i] = guess  # Replace "_" with correct guess
            return True
        else:
            return False

    def guess_word(guess, word):
        return guess.lower() == word.lower()

    def hangman(word_object):
        limbs = 5
        word = word_object["word"]
        hint = word_object["hint"]

        letters_list = list(word.lower())  # Convert to lowercase for case-insensitive matching
        letters_known = ["_" for _ in range(len(letters_list))]

        def play_game():
            hint_label.config(text="Hint: " + hint)
            word_label.config(text="Word to guess: " + " ".join(letters_known))
            play_button.config(state=tk.DISABLED)
            submit_button.config(state=tk.NORMAL)

        def submit_guess():
            nonlocal limbs
            guess = guess_entry.get().strip()
            guess_entry.delete(0, tk.END)

            if guess == "solve":
                solve_guess = solve_entry.get().strip().lower()
                if guess_word(solve_guess, word):
                    result_label.config(text="Good job! The word was " + word)
                else:
                    limbs -= 1
                    if limbs <= 0:
                        result_label.config(text="You ran out of guesses. The correct word was " + word)
            elif len(guess) == 1:
                if guess_letter(guess, letters_list, letters_known, limbs):
                    word_label.config(text="Word to guess: " + " ".join(letters_known))
                    if "_" not in letters_known:
                        result_label.config(text="Good job! The word was " + word)
                else:
                    limbs -= 1
                    if limbs <= 0:
                        result_label.config(text="You ran out of guesses. The correct word was " + word)
            else:
                result_label.config(text="You did not provide a valid input.")

            limbs_label.config(text="Limbs remaining: " + str(limbs))

        # Create the game GUI
        game_frame = tk.Frame(root)

        hint_label = tk.Label(game_frame, text="Hint: " + hint)
        hint_label.pack(pady=10)

        word_label = tk.Label(game_frame, text="Word to guess: " + " ".join(letters_known))
        word_label.pack(pady=10)

        guess_entry = tk.Entry(game_frame)
        guess_entry.pack(pady=5)

        submit_button = tk.Button(game_frame, text="Submit Guess", command=submit_guess, state=tk.DISABLED)
        submit_button.pack(pady=10)

        solve_entry = tk.Entry(game_frame)
        solve_entry.pack(pady=5)

        solve_button = tk.Button(game_frame, text="Solve", command=lambda: submit_guess("solve"))
        solve_button.pack(pady=10)

        limbs_label = tk.Label(game_frame, text="Limbs remaining: " + str(limbs))
        limbs_label.pack(pady=10)

        result_label = tk.Label(game_frame, text="")
        result_label.pack(pady=10)

        play_button = tk.Button(game_frame, text="Play Again", command=play_game)
        play_button.pack(pady=10)

        play_game()

        game_frame.pack()

    # Create the main window
    root = tk.Tk()
    root.title("Hangman Game")

    # Start frame
    hangman_frame = tk.Frame(root)
    start_button = tk.Button(hangman_frame, text="Start Game", command=lambda: hangman(random.choice(wBank)))
    start_button.pack(pady=20)
    hangman_frame.pack()

    root.mainloop()

# Run the hangman game with GUI
hangman_game()
