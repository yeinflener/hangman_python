import random
from hangman_words import word_list
from hangman_art import logo, stages

#print logo from hangman_art.py and print it at start of game.
print(logo)

# Create word_list for initial testing.
# word_list = ["camp", "moon", "star", "break"]

# Generate a random word from word_list in hangman_words file and
# assign it to a variable called random_chosen_word
random_chosen_word = random.choice(word_list)
# print(f"For testing purposes, the chosen word is: {random_chosen_word}")

end_of_game = False
# Set 'lives' to equal 6
lives = 6

# Create an empty list called display_chosen_word
display_chosen_word = []
# For each letter in the random_chose_word, add a "_" to display,
# representing each letter to guess.
for _ in range(len(random_chosen_word)):
    display_chosen_word += "_"
# print(display_chosen_word)

# Use a while loop to let user guess again.
while not end_of_game:
    # User to input a guess letter
    guess = input("Guess a letter: ").lower()
    # when user entered the same correct guess letter, let user know
    if guess in display_chosen_word:
        print(f"You've already guessed {guess}!! ")

    # Loop through each position in the random_chosen_word.
    # If guessed letter at that position matches "guess", then reveal it
    # in the display at the corresponding position.
    for position in range(len(random_chosen_word)):
        if random_chosen_word[position] == guess:
            display_chosen_word[position] = random_chosen_word[position]
    # print(display_chosen_word)
    # Join all the elements in the list and convert it into a String.
    delimiter = ""
    chosen_word_string = delimiter.join(display_chosen_word)
    print(f"Word to guess: {chosen_word_string}")

    # If guess is not a letter in the random_chosen_word, reduce 'lives' by 1.
    # If 'lives' goes down to 0, game stops, and prints "You lose!"
    if guess not in random_chosen_word:
        lives = lives - 1
        print(f"You guessed {guess}, that is not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print(f"The word was: {random_chosen_word}. You lost!!!!! ")

    # inform user number of lives left in the game
    print(f"**************** Lives remaining: {lives}/6 ****************")

    # if all blanks have been filled with correct guess letters, user wins the game
    if '_' not in display_chosen_word:
        end_of_game = True
        print("You win!!!!!")

    # Print ASCII art from 'stages' in hangman_art.py file.
    # The 'stages' corresponds to the current number of 'lives' user has left.
    print(stages[lives])











