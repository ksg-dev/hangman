import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
display = []
lives = 6
#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

chosen_word = random.choice(word_list)

for i in range(len(chosen_word)):
    display.append("_")

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
end_of_game = False
#current_stage = 0
print(stages.pop(-1))
while not end_of_game:
    guess = input("Guess a letter: ").lower().strip()
    slot = 0
    if guess not in chosen_word:
        lives -= 1
        print(stages.pop(-1))
    for i in chosen_word:
        if guess == i:
            display[slot] = i
            slot += 1
        else:
            slot += 1
    print(f"{' '.join(display)}")
    print(lives)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
    elif lives == 0:
        end_of_game = True
        print("YOU LOSE")

