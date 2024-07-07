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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarter_val = 0.25
dime_val = 0.10
nickle_val = 0.05
penny_val = 0.01

def get_cash():
    print("Please insert coins.")
    quarters = input("How many quarters?: ")
    dimes = input("How many dimes?: ")
    nickles = input("How many nickles?: ")
    pennies = input("How many pennies?: ")
    total_cash = (int(quarters) * quarter_val + int(dimes) * dime_val
                  + int(nickles) * nickle_val + int(pennies) * penny_val)
    return round(total_cash, 2)

def prepare(total_cash, coffee_type):
    if total_cash < MENU[coffee_type]["cost"]:
        print("Not enough money!")
        return

    ingredients = MENU[coffee_type]["ingredients"]

    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Not enough: {ingredient}")
            return
        resources[ingredient] -= ingredients[ingredient]

    change = round(total_cash - MENU[coffee_type]["cost"], 2)
    print(f"Here is ${change} in change.")
    print(f"Here is your {coffee_type}. Enjoy!")


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino):\n")
    match user_input:
        case "report":
            print(f"Water: {resources["water"]}")
            print(f"Milk: {resources["milk"]}: ")
            print(f"Coffee: {resources["coffee"]}: ")
        case "espresso" | "latte" | "cappuccino":
            total_cash = get_cash()
            prepare(total_cash, user_input)
        case "off":
            break
        case _:
            print(f"Sorry {user_input} invalid input.")
