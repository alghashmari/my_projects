# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
# from xml.sax.handler import property_lexical_handler

bill = float(input("what was the total bill? $"))
people = int(input("what number of people"))
tip = int(input("what is the percentage? 15 12 10"))

tip_percentage = tip / 100
total_tip_percentage = bill * tip_percentage
total_bill = bill * total_tip_percentage
final_amount = round(total_bill, 2)
print(f"amout per pesron {final_amount}$")
