print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: Work out how much they need to pay based on their choice
# todo: Work out how much to add to their bill based on their pepperoni choice
# todo: Work out their final amount based on whether they want to add cheese

# Considers what type of pizza is selected
if size == "S":
    price = 15
if size == "M":
    price = 20
if size == "L":
    price = 25

# Checks to see if they added pepperoni and to add up the cost if its small its +2 and if its medium or large its +3 to the final price
if pepperoni == "Y":
    if size == "S":
        price = price + 2
    elif size in ["M", "L"]:
        price = price + 3


# Checks to see if the user added extra_cheese and adds up the cost to the final price
if extra_cheese == "Y":
    price = price + 1

# Prints out the final result of the price
print(f"your final bill is: ${price}.")

