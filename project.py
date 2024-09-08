import random 
# Adding words that are going to be checked

words_list = ["ENGLAND", "GERMANY", "SCOTLAND", "CANADA", "MALTA", "SWEDEN"]

# Pick a random word
chosen_word = random.choice(words_list) 
print(chosen_word)


# lives of the character
lives = 5

is_game_over = False

#chosen = SWEDEN
display = [] # []
# Show letter block 
for i in range(len(chosen_word)): #0 - 5
    display += "_" 
