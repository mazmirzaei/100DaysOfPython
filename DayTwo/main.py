print("Welcome to the Tip Calculator")

# Getting user inputs
try:
    total_amount = float(input("What was the total bill? $"))
    tip = float(input("What percentage tip would you like to give? 10, 12, 15 or another value? "))
    people = int(input("How many people to split the bill? "))

    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")

    # Calculating total amount with tip
    tip_percent = tip / 100
    total_with_tip = total_amount * (1 + tip_percent)

    # Splitting the total amount
    split_amount = round(total_with_tip / people, 2)
    # Ensuring the split amount is correctly formatted to two decimal places
    split_amount = "{:.2f}".format(split_amount)

    print(f"Each person should pay: ${split_amount}")

except ValueError as e:
    print(f"Invalid input: {e}")
