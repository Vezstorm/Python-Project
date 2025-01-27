print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print("The ticket will cost you 12 OMR")
    elif age > 12 < 18:
        print("The ticket will be 7 OMR")
    else:
        print("The ticket will cost you 5 OMR")
else:
    print("Sorry you have to grow taller before you can ride.")


# We can use elif as many times as we like
# A nested if statement would be written inside the original if statement with and is indented
# An Elif statement would be written inside the nested if statement and does not require and else
