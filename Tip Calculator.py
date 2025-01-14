print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? OMR"))
tip = int(input("How much tip would you like to give? 10 , 12 or 15?"))
people = int(input("How many people would like to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: OMR {final_amount}")

# Notes
# tip_as_percent converts the tip percentage into decimal form for example 10 is 0.10, 12 is 0.12 and 15 is 0.15
# total_tip_amount multiplies the bill by the tip as percentage variable (TIP PERCENTAGE)
# total_bill adds the total_tip_amount variable to the original bill variable to get the total bill and store it in total_bill variable
# bill_per_person divides the total_bill variable by the number of people whom are splitting the bill
# final_amount rounds the amount each person would need to pay and rounds the output to two decimal places
