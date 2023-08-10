from Person import Person
from Staff import Staff


class Order:
    menu = {"1": ["De Anza Burger", 5.25, 0], "2": ["Bacon Cheese", 5.75, 0],
            "3": ["Mushroom Swiss", 5.95, 0], "4": ["Western Burger", 5.95, 0],
            "5": ["Don Cali Burger", 5.95, 0]}

    def __init__(self):
        a = 0

    def print_menu(self):
        '''Prints out the menu and its prices, and returns an "order sheet"'''

        print("-----------MENU-----------")
        for i in self.menu:
            print("#{} {}: ${}".format(i, self.menu[i][0], self.menu[i][1]))
        return self.menu

    def accept_order(self):
        '''Accepts a dictionary "order", and prompts the user to enter their desired item and amount,
           checking for validity and adding it to the order.'''
        order = 0
        while order != "6":
            order = input("Enter the number of your item, or 6 to end your order: ")
            if order in self.menu:
                valid_amount = False
                while not valid_amount:
                    amount = input("How many {}s do you want? ".format(self.menu[order][0]))
                    if amount.isnumeric() and int(amount) > 0:
                        self.menu[order][2] = self.menu[order][2] + int(amount)
                        print("{} {}s have been added to your order.".format(amount, self.menu[order][0]))
                        valid_amount = True
                    else:
                        print("This is an invalid amount. Please try again.")
            elif order == "6":
                print("Thank you for ordering!")
            elif order.isnumeric():
                print("This is an invalid item number. Please try again.")
            else:
                print("This doesn't seem to be a number... Please try again.")

    def price_calculate(self):
        '''This accepts the "order", and returns the total cost of the order, as well as the additional tax'''
        gross = 0
        tax = 0

        role = input("Are you a [student] or [staff]? ")
        while role != "student" and role != "staff":
            print("That is not a registered role.")
            role = input("Are you a [student] or [staff]? ")

        for i in self.menu:
            gross += (self.menu[i][1] * self.menu[i][2])

        if role == "staff":
            user = Staff()
            tax = user.Tax(gross)
        else:
            user = Person()
            tax = 0.00

        return gross, tax, user
