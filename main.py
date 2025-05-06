MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 1000,
    "milk": 500,
    "coffee": 300,
}

def chk_res(w,m,c,drink):
    if MENU[drink]["ingredients"]["water"]<=w and MENU[drink]["ingredients"]["milk"]<=m and MENU[drink]["ingredients"]["coffee"]<=c:
        return True
    else:
        print(f"{drink} is unavailable..please try another drink!!!")
        return False

def report(water,milk,coffee):
    print(f"Water:{water}")
    print(f"Milk:{milk}")
    print(f"Coffee:{coffee}")
def price_check(quarters,dimes,pennies,nickles,drink):
    sum_of_quarters=quarters * 0.25
    sum_of_dimes = dimes * 0.10
    sum_of_pennies = pennies * 0.01
    sum_of_nickels = nickles * 0.05
    amount=sum_of_dimes+sum_of_pennies+sum_of_nickels+sum_of_quarters
    print(f"You have paid {amount}$")
    extra=amount- MENU[drink]["cost"]
    if MENU[drink]["cost"]<=amount:
        print(f"Here is your rest of the change of {extra}")
        return True
    else:
        return False
order=input("What would you like? (espresso/latte/cappuccino):\n").lower()

while order!="off":

    avav_water = resources["water"]
    avav_milk = resources["milk"]
    avav_coffee = resources["coffee"]

    if chk_res(avav_water, avav_milk, avav_coffee, order) == True:
        qua = float(input("Enter the number of quarters\n"))
        dim = float(input("Enter the number of dimes\n"))
        pen = float(input("Enter the number of pennies\n"))
        nic = float(input("Enter the number of nickles\n"))
        if price_check(qua, dim, pen, nic, order) == True:
            print("Enjoy your drink!!")
            avav_water = resources["water"] - MENU[order]["ingredients"]["water"]
            avav_milk = resources["milk"] - MENU[order]["ingredients"]["milk"]
            avav_coffee = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
            resources["water"] = avav_water
            resources["milk"] = avav_milk
            resources["coffee"] = avav_coffee
            print(f"Remaining ingredients: {resources}")

        else:
            print("The amount is insufficient for the drink!!")
    else:
        print("This drink is unavailable at this moment...please try another!!")

    order = input("What would you like? (espresso/latte/cappuccino):\n").lower()








