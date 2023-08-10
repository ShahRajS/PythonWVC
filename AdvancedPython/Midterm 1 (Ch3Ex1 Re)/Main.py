# Raj Shah CIST005B Midterm 1 Project

from Order import Order


def main():
    new_order = Order()
    new_order.print_menu()
    new_order.accept_order()
    gross, tax, user = new_order.price_calculate()
    user.SaveToFile(new_order.menu, gross, tax)
    del user
    del new_order


if __name__ == "__main__":
    main()

'''
Test 1:

-----------MENU-----------
#1 De Anza Burger: $5.25
#2 Bacon Cheese: $5.75
#3 Mushroom Swiss: $5.95
#4 Western Burger: $5.95
#5 Don Cali Burger: $5.95
Enter the number of your item, or 6 to end your order: 1
How many De Anza Burgers do you want? 3
3 De Anza Burgers have been added to your order.
Enter the number of your item, or 6 to end your order: 3
How many Mushroom Swisss do you want? 1
1 Mushroom Swisss have been added to your order.
Enter the number of your item, or 6 to end your order: 7
This is an invalid item number. Please try again.
Enter the number of your item, or 6 to end your order: -1
This doesn't seem to be a number... Please try again.
Enter the number of your item, or 6 to end your order: two
This doesn't seem to be a number... Please try again.
Enter the number of your item, or 6 to end your order: 6
Thank you for ordering!
Are you a [student] or [staff]? blob
That is not a registered role.
Are you a [student] or [staff]? student
Your bill for today:
--------------------
[#1 De Anza Burger:  $5.25] x 3
[#3 Mushroom Swiss:  $5.95] x 1

Total before tax:   $21.70
			 Tax:   $0.00
Total Price:		$21.70

Process finished with exit code 0

Test 2:

-----------MENU-----------
#1 De Anza Burger: $5.25
#2 Bacon Cheese: $5.75
#3 Mushroom Swiss: $5.95
#4 Western Burger: $5.95
#5 Don Cali Burger: $5.95
Enter the number of your item, or 6 to end your order: 4
How many Western Burgers do you want? 10
10 Western Burgers have been added to your order.
Enter the number of your item, or 6 to end your order: 5
How many Don Cali Burgers do you want? 15
15 Don Cali Burgers have been added to your order.
Enter the number of your item, or 6 to end your order: 2
How many Bacon Cheeses do you want? 6
6 Bacon Cheeses have been added to your order.
Enter the number of your item, or 6 to end your order: 6
Thank you for ordering!
Are you a [student] or [staff]? staff
Your bill for today:
--------------------
[#2 Bacon Cheese:  $5.75] x 6
[#4 Western Burger:  $5.95] x 10
[#5 Don Cali Burger:  $5.95] x 15

Total before tax:   $183.25
			 Tax:   $16.49
Total Price:		$199.74

Process finished with exit code 0
'''
