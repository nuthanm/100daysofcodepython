# Program to calcuate how much tip and sharing calculation
print("Welcome to the tip calculator")
bill_in_float = float(input("What was the total bill? Rs: "))
tip_percentage = float(input("What percentage of amount tip you want to give? 10/20/30/any? "))
members = int(input("How many members want to share? "))

extra_amount_for_tip = (bill_in_float * (tip_percentage / 100))
print(extra_amount_for_tip)

final_amount = (bill_in_float + extra_amount_for_tip)
print(final_amount)
person_share = "{:.5f}".format(final_amount / members)
print(f"Each person should pay Rs: {person_share}")