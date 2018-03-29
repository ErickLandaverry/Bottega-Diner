def main():
    totalCost = 0
    print('''
    "Welcome to the Bottega Diner, where we serve your favorite munchies all day!"
    ''')
    name = input("What is your name?")
    print("Hello " + name + "!")
    print('''
     You get one entree and two side choices at regular cost.
    ''')

    answer = input("Would you like to try the house special? It is Cornflakes with Ketchup.").upper()
    if answer == "YES":
        print("Are you sure? It tastes like shit!")
    else:
        print("Good, because it tastes like shit!")

    print('''
    Here is our menu!
    ''')

    mainMenu(totalCost)


def mainMenu(totalCost):
    print("1.Sandwhich  $8.00")
    print("2.Hotdog  $7.50")
    print("3.Salad  $6.00")
    selection = int(input("Enter Choice:"))
    print("\n")
    if selection == 1:
        totalCost += Sandwhich(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    elif selection == 2:
        totalCost += Hotdog(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    elif selection == 3:
        totalCost += Salad(totalCost)
        totalCost += sideMenu(totalCost)
        receipt = "your total is $" + str(totalCost)
        print(receipt)
    else:
        print("Invalid choice. enter 1-3")
        mainMenu()


def Sandwhich(totalCost):
    print("Great choice!")
    totalCost += 8
    # anykey = input("Enter anything to go to side menu")
    return totalCost


def Hotdog(totalCost):
    print("You must be hungry!")
    totalCost += 7.5
    # anykey = input("Enter anything to go to side menu")
    return totalCost


def Salad(totalCost):
    print("Well, Shit someone is looking to be healthy! Are you sure you want this? Sounds like garbage to me!")
    totalCost += 6
    # anykey = input("Enter anything to go to side menu")
    return totalCost


def sideMenu(totalCost):
    print("1.Chips $10.50")
    print("2.Cookie $7.50")
    print("3.Fries $3")
    selection = int(input("Enter Choice:"))
    if selection == 1:
        totalCost += Chips(totalCost)
        return totalCost
    elif selection == 2:
        totalCost += Cookie(totalCost)
        return totalCost
    elif selection == 3:
        totalCost += Drink(totalCost)
        return totalCost
    else:
        print("Invalid choice. enter 1-3")
        sideMenu()


def Chips(totalCost):
    print("Oh, you fat ass! I'm proud of you. That'll be $10.50.")
    totalCost += 10.5
    # anykey = input("Enter anything to return to main menu")
    return totalCost


def Cookie(totalCost):
    print("A cookie it is! that'll be $7.50")
    totalCost += 7.5
    # anykey = input("Enter anything to return to main menu")
    return totalCost


def Drink(totalCost):
    print("Sweet!")
    totalCost += 3
    # anykey = input("Enter anything to return to main menu")
    return totalCost
    receipt = "your total is $" + str(totalCost)

main()
