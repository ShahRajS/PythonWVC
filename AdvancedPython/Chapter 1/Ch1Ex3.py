#Raj Shah
#CIST-005B-72148

#This program take an input of hours and pay rate, and computes the total amount owed
#calculating for overtime past 40 hours at a 1.5x rate to inputted rate. It checks for a
#valid numeric input, and catches if a value is negative when not possible.

import random
def get_input():
    valid_hours = False
    valid_rate = False
    company = input("Enter your company name: ")
    while (valid_hours == False):
        valid_hours = True
        hours = input("Enter the hours: ")
        try:
            hours_float = float(hours.strip())
        except ValueError:
            print("Error, please enter numeric input")
            valid_hours = False
    while (valid_rate == False):
        valid_rate = True
        rate = input("Enter the rate: ")
        try:
            rate_float = float(rate.strip())
        except ValueError:
            print("Error, please enter numeric input")
            valid_rate = False

    return hours_float, rate_float, company

def compute_pay(hours, rate):
    if (hours > 0 and hours <= 40 and rate >= 0):
        total_pay = hours * rate
    elif (hours > 40 and rate >= 0):
        total_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        total_pay = -1
    return total_pay

def print_output(company, hours, rate, gross):
    if(gross == -1):
        print("Invalid number of hours or pay rate.")
    else:
        print("\n\nCompany: {} \nhours: {} \nRate: ${:.2f} \n**********************************************\nYour "
              "document number is: {} \nYour {} gross pay is ${:.2f} dollars.".format(company, hours, rate, random.randint(1000, 2000), company, gross))
    return 0

def main():
    hours_float, rate_float, company = get_input()
    total_pay = compute_pay(hours_float, rate_float)
    print_output(company, hours_float, rate_float, total_pay)

if __name__ == "__main__":
    main()
'''
Enter your company name: Google
Enter the hours: 45
Enter the rate: 10


Company: Google 
hours: 45.0 
Rate: $10.00 
**********************************************
Your document number is: 1946 
Your Google gross pay is $475.00 dollars.
----------------------------------------------
Enter your company name: -45
Enter the hours: 20
Enter the rate: twenty
Error, please enter numeric input
Enter the rate: 20


Company: -45 
hours: 20.0 
Rate: $20.00 
**********************************************
Your document number is: 1655 
Your -45 gross pay is $400.00 dollars.
'''