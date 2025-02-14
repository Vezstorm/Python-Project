print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right"').lower()

# Choice 1
if choice1 == "left":
    choice2 = input('You are now stranded in a beach, do you choose to swim or wait? Type "swim" or "wait"').lower()
    # Choice 2
    if choice2 == "wait":
        # Choice 3
        choice3 = input('Which door are you going to pick? Type "yellow" or "red" or "blue"').lower()
        if choice3 == "yellow":
            print("You found the treasure!")
            print(r'''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
            ''')
        elif choice3 == "red":
            print("Burned by fire. Game Over!")
        elif choice3 == "blue":
            print("Eaten by monsters. Game Over!")
        else:
            print("Game Over!")
        choice4 = input('Hello pick y o r')

else:
    print("You fell into a hole. Game Over!")

# Notes:
# ASCII art is a form of text-based digital art that uses characters from the ASCII character set to create images and designs.
# It is often used in old-school computer graphics, email signatures, and creative coding.

# There are three single quotes (''') at the start and end of the ASCII Art
# The three single quotes allow you to create multiple lines of a string (Ensure to place 3 at the start and end)

# The word "You're" contains an apostrophe ('), which could break the string definition.
# To fix this, we use the escape character (\) before the apostrophe:
# 'You\'re'