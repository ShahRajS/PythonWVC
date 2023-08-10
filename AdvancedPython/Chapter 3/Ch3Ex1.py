# Raj Shah     CIST-005B-72148

# This program provides the burger menu at De Anza college, and lets the user select their order, and
# provides the expected cost of the order.

def print_menu():
    '''Prints out the menu and its prices, and returns an "order sheet"'''
    menu = {"1": ["De Anza Burger", 5.25, 0], "2": ["Bacon Cheese", 5.75, 0],
            "3": ["Mushroom Swiss", 5.95, 0], "4": ["Western Burger", 5.95, 0],
            "5": ["Don Cali Burger", 5.95, 0]}

    print("-----------MENU-----------")
    for i in menu:
        print("#{} {}: ${}".format(i, menu[i][0], menu[i][1]))
    return menu


def accept_order(menu):
    '''Accepts a dictionary "order", and prompts the user to enter their desired item and amount,
       checking for validity and adding it to the order.'''
    order = 0
    while order != "6":
        order = input("Enter the number of your item: ")
        if order in menu:
            valid_amount = False
            while not valid_amount:
                amount = input("How many {}s do you want? ".format(menu[order][0]))
                if amount.isnumeric() and int(amount) > 0:
                    menu[order][2] = menu[order][2] + int(amount)
                    print("{} {}s have been added to your order.".format(amount, menu[order][0]))
                    valid_amount = True
                else:
                    print("This is an invalid amount. Please try again.")
        elif order == "6":
            print("Thank you for ordering!")
        elif order.isnumeric():
            print("This is an invalid item number. Please try again.")
        else:
            print("This doesn't seem to be a number... Please try again.")


def price_calculate(order):
    '''This accepts the "order", and returns the total cost of the order, as well as the additional tax'''
    gross = 0
    tax = 0
    role = input("Are you a [student] or [staff]? ")
    while role != "student" and role != "staff":
        print("That is not a registered role.")
        role = input("Are you a [student] or [staff]? ")

    for i in order:
        gross += (order[i][1] * order[i][2])

    if role == "staff":
        tax = round(0.09 * gross, 2)

    return gross, tax


def print_receipt(order, gross, tax):
    '''This function prints out the "receipt" for the order'''
    print("Your bill for today:\n--------------------")
    for i in order:
        if order[i][2] > 0:
            print("[#{} {}:  ${}] x {}".format(i, order[i][0], order[i][1], order[i][2]))
    print(
        "\nTotal before tax:   ${:.2f}\n\t\t\t Tax:   ${:.2f}\nTotal Price:\t\t${:.2f}".format(gross, tax, gross + tax))


def main():
    order = print_menu()
    accept_order(order)
    gross, tax = price_calculate(order)
    print_receipt(order, gross, tax)


if __name__ == "__main__":
    main()

'''
-----------MENU-----------
#1 De Anza Burger: $5.25
#2 Bacon Cheese: $5.75
#3 Mushroom Swiss: $5.95
#4 Western Burger: $5.95
#5 Don Cali Burger: $5.95
Enter the number of your item: 1
How many De Anza Burgers do you want? 2
2 De Anza Burgers have been added to your order.
Enter the number of your item: 3
How many Mushroom Swisss do you want? 1
1 Mushroom Swisss have been added to your order.
Enter the number of your item: 7
This is an invalid item number. Please try again.
Enter the number of your item: -1
This doesn't seem to be a number... Please try again.
Enter the number of your item: two
This doesn't seem to be a number... Please try again.
Enter the number of your item: 6
Thank you for ordering!
Are you a [student] or [staff]? student
Your bill for today:
--------------------
[#1 De Anza Burger:  $5.25] x 2
[#3 Mushroom Swiss:  $5.95] x 1

Total before tax:   $16.45
			 Tax:   $0.00
Total Price:		$16.45

-----------MENU-----------
#1 De Anza Burger: $5.25
#2 Bacon Cheese: $5.75
#3 Mushroom Swiss: $5.95
#4 Western Burger: $5.95
#5 Don Cali Burger: $5.95
Enter the number of your item: 4
How many Western Burgers do you want? 10
10 Western Burgers have been added to your order.
Enter the number of your item: 5
How many Don Cali Burgers do you want? 15
15 Don Cali Burgers have been added to your order.
Enter the number of your item: 3
How many Mushroom Swisss do you want? 6
6 Mushroom Swisss have been added to your order.
Enter the number of your item: 6
Thank you for ordering!
Are you a [student] or [staff]? staff
Your bill for today:
--------------------
[#3 Mushroom Swiss:  $5.95] x 6
[#4 Western Burger:  $5.95] x 10
[#5 Don Cali Burger:  $5.95] x 15

Total before tax:   $184.45
			 Tax:   $16.60
Total Price:		$201.05

'''
