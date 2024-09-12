import random 
# Adding words that are going to be checked

words_list = [
    "AFGHANISTAN", "ALBANIA", "ALGERIA", "ANDORRA", "ANGOLA", "ANTIGUA-AND-BARBUDA", "ARGENTINA", "ARMENIA", "AUSTRALIA",
    "AUSTRIA", "AZERBAIJAN", "BAHAMAS", "BAHRAIN", "BANGLADESH", "BARBADOS", "BELARUS", "BELGIUM", "BELIZE", "BENIN",
    "BHUTAN", "BOLIVIA", "BOSNIA AND HERZEGOVINA", "BOTSWANA", "BRAZIL", "BRUNEI", "BULGARIA", "BURKINA FASO", "BURUNDI",
    "CABO VERDE", "CAMBODIA", "CAMEROON", "CANADA", "CENTRAL-AFRICAN-REPUBLIC", "CHAD", "CHILE", "CHINA", "COLOMBIA",
    "COMOROS", "CONGO", "COSTA-RICA", "CROATIA", "CUBA", "CYPRUS",
    "CZECH REPUBLIC", "DENMARK", "DJIBOUTI", "DOMINICA", "DOMINICAN-REPUBLIC", "EAST-TIMOR", "ECUADOR",
    "EGYPT", "EL SALVADOR", "EQUATORIAL GUINEA", "ERITREA", "ESTONIA", "ESWATINI", "ETHIOPIA", "FIJI", "FINLAND", "FRANCE",
    "GABON", "GAMBIA", "GEORGIA", "GERMANY", "GHANA", "GREECE", "GRENADA", "GUATEMALA", "GUINEA", "GUINEA-BISSAU", "GUYANA",
    "HAITI", "HONDURAS", "HUNGARY", "ICELAND", "INDIA", "INDONESIA", "IRAN", "IRAQ", "IRELAND", "ISRAEL", "ITALY",
    "IVORY-COAST", "JAMAICA", "JAPAN", "JORDAN", "KAZAKHSTAN", "KENYA", "KIRIBATI", "NORTH-KOREA", "SOUTH-KOREA",
    "KOSOVO", "KUWAIT", "KYRGYZSTAN", "LAOS", "LATVIA", "LEBANON", "LESOTHO", "LIBERIA", "LIBYA", "LIECHTENSTEIN",
    "LITHUANIA", "LUXEMBOURG", "MADAGASCAR", "MALAWI", "MALAYSIA", "MALDIVES", "MALI", "MALTA", "MARSHALL-ISLANDS",
    "MAURITANIA", "MAURITIUS", "MEXICO", "MICRONESIA", "MOLDOVA", "MONACO", "MONGOLIA", "MONTENEGRO", "MOROCCO", "MOZAMBIQUE",
    "MYANMAR", "NAMIBIA", "NAURU", "NEPAL", "NETHERLANDS", "NEW ZEALAND", "NICARAGUA", "NIGER", "NIGERIA",
    "NORTH-MACEDONIA", "NORWAY", "OMAN", "PAKISTAN", "PALAU", "PANAMA", "PAPUA NEW GUINEA", "PARAGUAY", "PERU", "PHILIPPINES",
    "POLAND", "PORTUGAL", "QATAR", "ROMANIA", "RUSSIA", "RWANDA", "SAINT-LUCIA",
    "SAMOA", "SAN-MARINO", "SAUDI-ARABIA", "SENEGAL", "SERBIA", "SEYCHELLES", "SIERRA-LEONE", "SINGAPORE",
    "SLOVAKIA", "SLOVENIA", "SOMALIA", "SOUTH-AFRICA", "SOUTH-SUDAN", "SPAIN", "SRI-LANKA", "SUDAN", "SURINAME",
    "SWEDEN", "SWITZERLAND", "SYRIA", "TAIWAN", "TAJIKISTAN", "TANZANIA", "THAILAND", "TOGO", "TONGA", "TUNISIA",
    "TURKEY", "TURKMENISTAN", "TUVALU", "UGANDA", "UKRAINE", "UAE", "UNITED-KINGDOM", "USA",
    "URUGUAY", "UZBEKISTAN", "VANUATU", "VATICAN-CITY", "VENEZUELA", "VIETNAM", "YEMEN", "ZAMBIA", "ZIMBABWE"
]
# Different stages
stages = ['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
 _______          

''', '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
 _______          

''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
 _______          

''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
 _______          

''', '''
    +---+
    |   |
    0   |
    |   |
        |
        |
 _______          

''',  '''
    +---+
    |   |
    0   |
        |
        |
        |
 _______          

''', '''
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

#chosen = SWEDEN
display = [] # []
# Show letter block 
for i in range(len(chosen_word)): #0 - 5
    display += "_" 


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