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

def main():
    profit = 0
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

    machine_running = True
    while machine_running:

        # Asks the user
        choice = input("What would you like? (espresso/latte/cappuccino) ")

        # Schow the report of the coffee machine
        if choice == "report":
            report(resources, profit)

        # Secret command for turnning off the machine
        elif choice == "off":
            machine_running = False
            print("Shutting down...")

        # User selected a drink from the menu
        elif choice in MENU:
            if check_recources(choice, resources):
                money_recieved = process_coins()
                if transaction(money_recieved, choice):
                    profit += MENU[choice]["cost"]
                    
                    # Substract the ingredients of the drink from the coffee machine
                    for item in resources:
                        resources[item] -= MENU[choice]["ingredients"][item]

                    print(f"Here is your {choice}. Enjoy!\n")
        
        # Invalid choice
        else:
            print("Invalid choice!")
                    

def report(resources, profit):
    '''Show recources in the coffee machine'''
    for item in resources:
        if item == "coffee":
            print(f"{item.capitalize()}: {resources[item]}g")
        else:
            print(f"{item.capitalize()}: {resources[item]}ml")
    print(f"Money: ${round(profit, 2)}")


def check_recources(drink, resources):
    '''Checks if the machine has enough ingredients for the chosen drink'''
    for item in resources:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}!")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: ")) * 0.25
        dime = int(input("How many dimes?: ")) * 0.1
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

    except:
        quarters = 0
        dime = 0
        nickels = 0
        pennies = 0

    sum = quarters + dime + nickels + pennies

    return sum
    

def transaction(money_recieved, drink):
    '''Check if the inserted money is enough'''
    drink_cost = MENU[drink]["cost"]

    if money_recieved < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    else:
        print(f"Here is ${round(money_recieved - drink_cost, 2)} dollars in change.")

    return True


if __name__ == "__main__":
    main()