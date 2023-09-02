import json
import random

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
            print("Correct guess!")
        else:
            print("Incorrect guess.")
            limbs -= 1

        return limbs

    def guess_word(guess, word):
        return guess.lower() == word.lower()

    def hangman(word_object):
        limbs = 5
        word = word_object["word"]
        hint = word_object["hint"]
        print("Hint:", hint)

        letters_list = list(word.lower())  # Convert to lowercase for case-insensitive matching
        letters_known = ["_" for _ in range(len(letters_list))]

        print("Word to guess:", " ".join(letters_known))  # Display initial underscores

        while limbs > 0 and "_" in letters_known:
            var_guess = input("Guess a letter, a word, or 'solve': ").lower()

            if var_guess == "solve":
                solve_guess = input("Enter your guess to solve: ").lower()
                if guess_word(solve_guess, word):
                    print("Good job! The word was:", word)
                    return True  # End the game if solved correctly

            elif len(var_guess) == 1:
                limbs = guess_letter(var_guess, letters_list, letters_known, limbs)
            elif len(var_guess) < 1:
                var_guess = input("Invalid guess. Guess again: ").lower()
            else:
                print("You did not provide a valid input.")

            print("Hint:", hint)
            print("Limbs remaining:", limbs)
            print("Word to guess:", " ".join(letters_known))  # Display current progress

        print("The correct word was:", word)  # Display correct word
        return False  # Game over

    def custom_input():
        custom_word = input("Enter custom word here: ").lower()
        custom_hint = input("Enter custom hint here: ")
        word_object = {"word": custom_word, "hint": custom_hint}
        return hangman(word_object)

    def is_custom():
        is_custom = input("Enter 1 if you'd like to enter a custom word and hint to play with: ")
        if is_custom == "1":
            return custom_input()
        else:
            word_object = random.choice(wBank)
            return hangman(word_object)

    def is_play():
        while True:
            playing = input("Enter 1 to play hangman: ")
            if playing == "1":
                if not is_custom():
                    break
            else:
                break

    while True:
        is_play()
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again not in ["Y", "y", "1", 1]:
            print("Thank you for playing!")
            break

# Run the hangman game
hangman_game()