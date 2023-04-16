from machine_data import MENU
from machine_data import resources


def transaction(pr, q, d, n, p):
    total_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    change = total_money - MENU[pr]["cost"]
    return change


def report():
    for r in resources:
        if r == "water" or r == "milk":
            unit = "ML"

        elif r == "coffee":
            unit = "G"

        else:
            unit = "$"

        print(f"{r}: {resources[r]} {unit}")


def espresso():
    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    resources["money"] += MENU["espresso"]["cost"]
    print("Enjoy your espresso!")


def latte():
    resources["water"] -= MENU["latte"]["ingredients"]["water"]
    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
    resources["money"] += MENU["latte"]["cost"]
    print("Enjoy your latte!")


def cappuccino():
    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
    resources["money"] += MENU["cappuccino"]["cost"]
    print("Enjoy your cappuccino!")


process = "ask"

while process != "off":
    process = input("What would you like? Espresso is $1.5, Latte is $2.5, Cappuccino is $3: ")

    if process == "report":
        report()

    elif process == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            quarters = int(input("How many quarters do you insert: "))
            dimes = int(input("How many dimes do you insert: "))
            nickles = int(input("How many nickles do you insert: "))
            pennies = int(input("How many pennies do you insert: "))
            if transaction(process, quarters, dimes, nickles, pennies) >= 0:
                espresso()
                print(f"Your change is {transaction(process, quarters, dimes, nickles, pennies)}")
            else:
                print("Sorry, your money is not enough.")
        else:
            print("Sorry, I cannot prepare espresso due to insufficient material.")

    elif process == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"] and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
            quarters = int(input("How many quarters do you insert: "))
            dimes = int(input("How many dimes do you insert: "))
            nickles = int(input("How many nickles do you insert: "))
            pennies = int(input("How many pennies do you insert: "))
            if transaction(process, quarters, dimes, nickles, pennies) >= 0:
                latte()
                print(f"Your change is {transaction(process, quarters, dimes, nickles, pennies)}")
            else:
                print("Sorry, your money is not enough.")
        else:
            print("Sorry, I cannot prepare latte due to insufficient material.")

    elif process == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"] and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
            quarters = int(input("How many quarters do you insert: "))
            dimes = int(input("How many dimes do you insert: "))
            nickles = int(input("How many nickles do you insert: "))
            pennies = int(input("How many pennies do you insert: "))
            if transaction(process, quarters, dimes, nickles, pennies) >= 0:
                cappuccino()
                print(f"Your change is {transaction(process, quarters, dimes, nickles, pennies)}")
            else:
                print("Sorry, your money is not enough.")
        else:
            print("Sorry, I cannot prepare cappuccino due to insufficient material.")

    elif process == "off":
        print("Goodbye!")

    else:
        print("Please make a valid selection!")