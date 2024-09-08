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


print(display)

# Accepting input from user
while is_game_over == False:
    user_input = input("Guess a letter:") #user_input = 'S'

    for position in range(len(chosen_word)): # 0 - 5
        letter = chosen_word[position] 
        if user_input == letter:
            display[position] = letter

    print(display)
  
    # If letter does not exist in the chosen word 
    if user_input not in chosen_word:
        #decrease a life 
        lives -= 1
        if lives == 0: 
            # User lost 
            is_game_over = True 
            print("You died!")     
    
