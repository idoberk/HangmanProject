import random
from hangman_words import word_list
from hangman_art import stages, logo

display = []
guessed_letters = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

for index in range(word_length):
    display.append("_")

display_word = "".join(display)

print(f"{logo}\n")
print(f"{display}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"The letter '{guess}' was already used.\n")
        continue
    else:
        guessed_letters.append(guess)

        for index in range(word_length):
            character = chosen_word[index]
            if guess == character:
                display[index] = character
                display_word = "".join(display)
        if guess not in chosen_word:
            lives -= 1
            print(stages[lives])
            print(f"The letter '{guess}' is not in the word.\n")
        print(f"{display}\n")
        if lives == 0:
            end_of_game = True
            print("You ran out of lives, you lose!")
            print(f"The word was \"{chosen_word}\"")
    if "_" not in display:
        end_of_game = True
        print("You win!")