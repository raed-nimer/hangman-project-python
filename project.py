import random 
# Adding words that are going to be checked

easy_words = ['ALBANIA', 'ALGERIA', 'ANDORRA', 'ANGOLA', 'ARMENIA',
 'AUSTRIA', 'BAHAMAS', 'BAHRAIN', 'BELARUS', 'BELGIUM', 'BELIZE', 'BENIN', 'BHUTAN',
  'BOLIVIA', 'BOTSWANA', 'BRAZIL', 'BRUNEI', 'CANADA', 
 'CHAD', 'CHILE', 'CHINA', 'CROATIA', 'CUBA', 'CYPRUS', 'DENMARK', 'DJIBOUTI', 'ECUADOR', 
'EGYPT', 'ESTONIA', 'ESWATINI', 'ETHIOPIA', 'FIJI', 'FINLAND', 'FRANCE', 
'GABON', 'GAMBIA', 'GEORGIA', 'GHANA', 'GREECE', 'GRENADA', 'GUINEA', 'GUYANA', 'HAITI', 'HUNGARY',
 'ICELAND', 'INDIA', 'IRAN', 'IRAQ', 'ISRAEL', 'ITALY', 'JAMAICA', 
 'JAPAN', 'JORDAN', 'KENYA', 'KOSOVO', 'KUWAIT', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO',
 'LIBERIA', 'LIBYA', 'MALAWI', 'MALI', 'MALTA', 'MEXICO', 'MONACO', 'NAMIBIA', 'NAURU', 'NEPAL', 'NIGER', 'OMAN',
 'PALAU', 'PANAMA', 'PERU', 'POLAND', 'QATAR', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAMOA', 'SERBIA',
  'SINGAPORE', 'SLOVAKIA', 'SOMALIA', 'SPAIN', 'SUDAN', 'SWEDEN', 'SYRIA', 'TAIWAN',
   'TOGO', 'TONGA', 'TUNISIA', 'TURKEY', 'TUVALU', 'UGANDA', 'UAE', 'USA', 'URUGUAY', 'VIETNAM', 'YEMEN', 'ZAMBIA']

medium_words = ['AFGHANISTAN', 'ARGENTINA', 'AUSTRALIA', 'AZERBAIJAN', 'BANGLADESH', 'BARBADOS', 'BULGARIA', 'BURUNDI', 
'CAMBODIA', 'CAMEROON', 'COLOMBIA', 'COMOROS', 'COSTA-RICA', 'DOMINICA', 'EQUATORIAL GUINEA', 'ERITREA', 'GUATEMALA', 
'GUINEA-BISSAU', 'HONDURAS', 'INDONESIA', 'IVORY-COAST', 'KAZAKHSTAN', 'KYRGYZSTAN', 'LIECHTENSTEIN', 'LITHUANIA', 
'LUXEMBOURG', 'MADAGASCAR', 'MALAYSIA', 'MALDIVES', 'MICRONESIA', 'MOLDOVA', 'MONGOLIA', 'MOROCCO', 'MOZAMBIQUE', 
'MYANMAR', 'NETHERLANDS', 'NICARAGUA', 'NIGERIA', 'NORWAY', 'PAKISTAN', 'PARAGUAY', 'PHILIPPINES', 'PORTUGAL', 
'SAINT-LUCIA', 'SAN-MARINO', 'SAUDI-ARABIA', 'SENEGAL', 'SEYCHELLES', 'SIERRA-LEONE', 'SLOVENIA', 'SRI-LANKA', 
'SURINAME', 'SWITZERLAND', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'TURKMENISTAN', 'UKRAINE', 'UZBEKISTAN', 'VANUATU',
 'VENEZUELA', 'ZIMBABWE']

hard_words = ['ANTIGUA-AND-BARBUDA', 'BOSNIA-AND-HERZEGOVINA', 'BURKINA-FASO', 'CENTRAL-AFRICAN-REPUBLIC', 
'CZECH-REPUBLIC', 'DOMINICAN-REPUBLIC', 'EAST-TIMOR', 'EL-SALVADOR', 'MARSHALL-ISLANDS', 'MAURITANIA', 'MAURITIUS',
 'NEW-ZEALAND', 'NORTH-MACEDONIA', 'NORTH-KOREA', 'PAPUA-NEW-GUINEA', 'SOUTH-AFRICA', 'SOUTH-KOREA', 'SOUTH-SUDAN', 
 'UNITED-KINGDOM', 'VATICAN-CITY']
print("\t!\tWELCOME TO HANGMAN\t!\n")
print("CHOOSE DIFFICULTY:")
print("1: EASY\n2: MEDIUM\n3: HARD\n")

difficulty_level = int(input("ENTER CHOICE:"))
if difficulty_level == 1: 
    words_list = easy_words
elif difficulty_level == 2:
    words_list = medium_words
elif difficulty_level == 3:
    words_list = hard_words    

# Different stages
stages = [ r''' 
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
 _______          

''', r'''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
 _______          

''', r'''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
 _______          

''', r'''
    +---+
    |   |
    0   |
   /|   |
        |
        |
 _______          

''', r'''
    +---+
    |   |
    0   |
    |   |
        |
        |
 _______          

''',  r'''
    +---+
    |   |
    0   |
        |
        |
        |
 _______          

''', r'''
    +---+
    |   |
        |
        |
        |
        |
 _______          

''']

# Pick a random word
chosen_word = random.choice(words_list) 



# lives of the character
lives = 5

is_game_over = False

display = []
# Show letter block
for i in range(len(chosen_word)):  # 0 - 5
    if chosen_word[i] == "-":
        display += "-" 
    else: 
        display += " "


print(display)

# Accepting input from user
while is_game_over == False:
    user_input = str(input("Guess a letter:")).upper() #user_input = 'S'
    # validating user_input
    if not user_input.isalpha():
        print("Only letters allowed")
        continue

    for position in range(len(chosen_word)): # 0 - 5
        letter = chosen_word[position] 
        if user_input == letter:
            display[position] = letter

    print(display)
  
    # If letter does not exist in the chosen word 
    if user_input not in chosen_word:
        #decrease a life 
        lives -= 1
        print("Oops! wrong guess. " + str(lives) + " Lives left")
        if lives == 0: 
            # User lost 
            is_game_over = True 
            print("You died!")     
    
    if '_' not in display:
        is_game_over = True 
        print("You won!")