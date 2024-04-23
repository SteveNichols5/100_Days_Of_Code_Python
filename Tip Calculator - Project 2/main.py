#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

total_bill = float(input("What is the total bill amount? \n"))
print(f"The total bill is ${total_bill:.2f}.")

guests = int(input("How many people are splitting the bill? \n"))
print(f"Alright, {guests} people are splitting the bill.")

tip_percent = float(input("How much of a tip would you like to leave? (ex. 10 12 or 15) \n"))
print(f"You'd like to leave a {tip_percent:.2f}% tip, confirmed.")

tip_decimal = float((tip_percent / 100))
#print(tip_decimal)
bill_with_tip = total_bill * (1 + tip_decimal)
bill_with_tip = float(bill_with_tip)
print(f"You adjusted bill with tip is ${bill_with_tip:.2f}.")

per_person = float(round(bill_with_tip / guests, 2))
print(f"Each person in your party should pay ${per_person:.2f}.")

print("Thank you for using the tip calculator, press enter to exit")
input()