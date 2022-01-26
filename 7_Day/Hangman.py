word_list = ["ananas", "mate", "honor", "ardvark", "camel", "feral"]

stages = ['''
   +---+
   |   |
   0   |
  /|\  |
  / \  |
       |
=========
''', '''
   +---+
   |   |
   0   |
  /|\  |
  /    |
       |
=========
''', '''
   +---+
   |   |
   0   |
  /|\  |
       |
       |
=========
''', '''
   +---+
   |   |
   0   |
  /|   |
       |
       |
=========
''', '''
   +---+
   |   |
   0   |
   |   |
       |
       |
=========
''', '''
   +---+
   |   |
   0   |
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

# Randomly choose a word from the word_list and 
# assing it to a variable called chosen_word.
lives = 6
import random
chosen_word = random.choice(word_list)

# Create an empty list called display.
# For each letter in the cosen_word, add a "_" to 'display'.
# So if the cosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

# Ask the user to guess a letter and assign their 
# answer to a variable called guess. Make guess lowercase.
end_of_game = False

while not end_of_game:
    
    guess = input("Gueess a letter: ").lower()[0]

 # loop through each position in the chosen_word; 
 # If the letter at that position matches 'guess' then reveal tht letter in the display at that position.
 # e. g. If the user huessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]
 # Check if the letter the iser guessed (guess) is one of 
 # the leters in the chosen_word.

    for position in range(word_length):
       char = chosen_word[position]
       # print(f"Current position: {position}\n Current letter: {char}\n Guessed letter: {guess}")
       if char == guess:
         display[position] = char

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            
    print(f"{' '.join(display)}")
# Print 'display' and you should see the guessed letter in the correct position and evety other letter replace with "_".

    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])