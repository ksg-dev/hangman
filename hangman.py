import random
from hangman_words import word_list
from hangman_art import stages, logo



display = []
lives = 6
guesses = []

chosen_word = random.choice(word_list)

for i in range(len(chosen_word)):
    display.append("_")

print(logo)
# Testing Code
print(f'Pssst, the solution is {chosen_word}.')

end_of_game = False

print(stages.pop(-1))
while not end_of_game:
    guess = input("Guess a letter: ").lower().strip()
    slot = 0
   
    if guess in guesses:
        print(f"You've already guessed this letter: {guess}")
    else:
        guesses.append(guess)
    
        if guess not in chosen_word:
            lives -= 1
            print(stages.pop(-1))
            print(f"Oops! The letter {guess} is not in the word. You have {lives} lives remaining.")
        for i in chosen_word:
            if guess == i:
                display[slot] = i
                slot += 1
            else:
                slot += 1
    print(f"{' '.join(display)}")
    

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
    elif lives == 0:
        end_of_game = True
        print("YOU LOSE")

