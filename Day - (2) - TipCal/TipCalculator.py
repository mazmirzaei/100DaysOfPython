#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

bill=float(input("How much was the bill: "))
people= int(input("How many people was there ? "))
tip = float(input("tip for ex. 0.12 for 12% : "))
def tip_calculator(bill,people,tip):
    each_person = 0
    minimum=0
    if bill > minimum:
        tip_bill = (bill * tip)
        total = bill + tip_bill
        each_person = round((total / people),3)
        return f"Each person should pay {each_person} dollars"
    else:
        return "Not to pay "

print(tip_calculator(bill,people,tip))