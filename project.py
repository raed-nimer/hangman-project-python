import pyfiglet
from colored import fg, attr
import random
import os
import time
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

def clear_screen(): 
  # Check the operating system and clear the screen accordingly 
  if os.name == 'nt': 
    # For Windows 
    os.system('cls') 
  else: # For macOS and Linux 
    os.system('clear')

# colored variables
OR = fg("orange_3") # Orange
CY = fg("cyan") # Cyan 
MG = fg("magenta") # Magenta 
PK = fg("pink_1") # Pink 
SB = fg("sky_blue_1") # Sky Blue 
# LV = fg("lavender_blush_1") # Lavender 
# DG = fg("dark_sea_green_4") # Dark Sea Green 
# BR = fg("brown_4") # Brown 
# DB = fg("deep_sky_blue_4") # Deep Sky Blue
GR = fg("dark_olive_green_2") 
RD = fg("light_red") 
GD = fg("gold_3a") 
YL = fg("light_yellow")
R = attr("reset")

INITIAL_BANNER = SB + pyfiglet.figlet_format(
    "WELCOME TO HANGMAN!", font="rectangles", justify="center"
    ) + R 
SUCCESS_MESSAGE = GR + pyfiglet.figlet_format(
    "YOU WON!", font="rectangles", justify="center"
    ) + R 
LOSE_MESSAGE = RD + pyfiglet.figlet_format(
    "YOU LOST!", font="rectangles", justify="center"
    ) + R 
print(INITIAL_BANNER)
print("CHOOSE DIFFICULTY:")
print("1: EASY\n2: MEDIUM\n3: HARD\n")

difficulty_level = int(input("ENTER CHOICE:\n"))
if difficulty_level == 1: 
    words_list = easy_words
elif difficulty_level == 2:
    words_list = medium_words
elif difficulty_level == 3:
    words_list = hard_words    

# Adding two seconds delay 
time.sleep(2)    
# Call the function to clear the screen 
clear_screen()

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
lives = 6

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
while is_game_over is False:
    print( GD + stages[lives] + R)
    user_input = str(input("Guess a letter: \n")).upper()  # user_input = 'S'
    # validating user_input
    if not user_input.isalpha():
        print("Only letters allowed")
        continue

    for position in range(len(chosen_word)):  # 0 - 5
        letter = chosen_word[position] 
        if user_input == letter:
            display[position] = letter

    print(display)

    # If letter does not exist in the chosen word 
    if user_input not in chosen_word:
        lives -= 1  # decrease a life 
        print("Oops! wrong guess. " + str(lives) + " Lives left")
        if lives == 0: 
            # User lost 
            is_game_over = True 
            time.sleep(2)
            clear_screen()
            print(LOSE_MESSAGE)   
            print("Country name was: " + chosen_word)

    if ' ' not in display:
        is_game_over = True 
        time.sleep(2)
        clear_screen()
        print(SUCCESS_MESSAGE)
