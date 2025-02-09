# Task Requirements:
# Based on a user's order, work out their final bill. Use the input() function to get a user's preferences and then add up the total for their order and tell them how much they have to pay.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

# todo: Work out how much they need to pay based on their choice
# todo: Work out how much to add to their bill based on their pepperoni choice
# todo: Work out their final amount based on whether they want to add cheese

print("Welcome to Python Pizza!")
size = input("Please type a size from the following options, S, M, L")
pepperoni = input("Would you like to add pepperoni? Type Y or N")
extra_cheese = input("Would you like to add extra cheese? Type Y or N")

bill = 0

# Size
if size.upper() == "S":
    bill =  15
elif size.upper() == "M":
    bill  = 20
elif size.upper() == "L":
    bill = 25
else:
    print("Please type one of the three options so we can calculate your final bill.")

# Pepperoni
if size.upper() == "S" and pepperoni.upper() == "Y":
    bill = bill + 2
if size.upper() in ['M', 'L'] and pepperoni.upper() == "Y":
    bill = bill + 3

# Extra Cheese
if extra_cheese.upper() == "Y":
    bill = bill + 1
    

print(f"Your final bill is ${bill}.")



