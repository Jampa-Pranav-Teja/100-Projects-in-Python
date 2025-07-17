print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
at = bill + (tip/100)*bill
people = int(input("How many people to split the bill? "))
pay = at/people
print(f"Each person must pay: {round(pay, 2)}")
