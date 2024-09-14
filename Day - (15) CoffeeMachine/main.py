MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_recourses_sufficent(order_ingredients):
    """Returns True when order can be made, False if ingredients not efficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry there is not enough {item}')
            is_enough = False
    return is_enough


def process_coins():
    """Returns total calculated from coins inserted"""
    print('insert coins')
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickels? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    print(f"You inserted ${total}")
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if the monet is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is the change ${change}')
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ')


machine_status = True
while machine_status:
    print("The Menu : Espresso $1.5, Latte $2.5, Cappuccino $3.0")
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice == 'off':
        machine_status = False
    elif choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${money}")
    else:
        drink = MENU[choice]
        # if true
        if is_recourses_sufficent(drink['ingredients']):
            # calls the function and store the total inside the payment
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])













