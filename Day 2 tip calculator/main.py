#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? €"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
tip = tip_percentage / 100
peeps = int(input("How many people to split the bill? "))
grande_totale = (1+tip)*total
#print((grande_totale))
per_person = grande_totale / peeps
per_person = "{:.2f}".format(per_person)

print(f"Each person should pay:€{per_person}") 
#formatting: to show 2 decimals even if the calculation result has less than 2 decimals. syntax: print(" jotain tekstii ja %.2f" % variable), or create str x = "{:.2f}".format(variable)