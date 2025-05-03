coffee_menu = {
    "latte"  :{ "water": 100, "coffee": 76, "money":2.5, "milk": 100},
    "espresso" : {"water": 150, "coffee": 80, "money":3, "milk": 120},
    "cappuccino" : {"water": 200, "coffee": 90, "money":4, "milk": 160},
}

resources = {
    "water": 500,
    "coffee": 300,
    "milk": 500,
    "money": 10
}
def payment_process(cust_input):
    pennies = int(input("Enter how many pennies: "))
    dimes = int(input("Enter how many dimes: "))
    nickel = int(input("Enter how many nickel: "))
    quaters = int(input("Enter how many quaters: "))
    total = pennies*0.01 + nickel*0.05 + dimes*0.10 + quaters*0.25
    if(total > coffee_menu[cust_input]["money"]):
        change = total - coffee_menu[cust_input]["money"]
        resources["water"] = resources["water"] - coffee_menu[cust_input]["water"]
        resources["coffee"] = resources["coffee"] - coffee_menu[cust_input]["coffee"]
        resources["milk"] = resources["milk"] - coffee_menu[cust_input]["milk"]
        resources["money"] = resources["money"] + coffee_menu[cust_input]["money"]
        print(f"Here is your change {change:.2f} \nHere is your coffee {cust_input} ☕ Have a nice day")
        print("\n")
        ask_the_user()
    else:
        print("Sorry that's not enough money. Money refunded 💵.")
        print("\n")
        ask_the_user()


def check_resources(cust_input):
    if(cust_input == "report"):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
        print("\n")
        ask_the_user()
    elif cust_input in coffee_menu:
        if coffee_menu[cust_input]["water"] <= resources["water"] and coffee_menu[cust_input]["coffee"] <= resources["coffee"] and coffee_menu[cust_input]["milk"] <= resources["milk"]:
            payment_process(cust_input)
        else:
            if coffee_menu[cust_input]["water"] > resources["water"]:
                print("Sorry, not enough water.")
            elif coffee_menu[cust_input]["milk"] > resources["milk"]:
                print("Sorry, not enough milk.")
            elif coffee_menu[cust_input]["coffee"] > resources["coffee"]:
                print("Sorry, not enough coffee.")
            else:
                payment_process(cust_input)

    elif cust_input == "off":
        print("Turning off the machine. Goodbye!")
        return
    else:
        print("Wrong input")
        ask_the_user()
    
def ask_the_user():
    cust_input = input("What coffee do you want? \n 1)Latte - $2.5 \n 2)espresso - $3 \n 3)cappuccino - $4 \n Enter Your Choice: ").lower()
    check_resources(cust_input)


ask_the_user()