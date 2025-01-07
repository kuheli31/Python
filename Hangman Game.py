import random
from hangman_stages import stages  # Import the stages

word_list = ["apple", "beautiful", "potato"]
lives = 6

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

game_over = False

while not game_over:
    print(stages[6 - lives])  # Print the hangman stage based on remaining lives
    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guessed_letter:
                display[position] = guessed_letter
        print(display)
    else:
        lives -= 1
        print(f"Incorrect guess! Lives remaining: {lives}")
        if lives == 0:
            game_over = True
            print("You lose!!!")

    if '_' not in display:
        game_over = True
        print("You win!!")
