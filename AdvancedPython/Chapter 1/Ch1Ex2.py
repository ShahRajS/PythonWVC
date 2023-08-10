#Raj Shah
#CIST-005B-72148

#This program take an input of hours and pay rate, and computes the total amount owed
#calculating for overtime past 40 hours at a 1.5x rate to inputted rate. It checks for a
#valid numeric input, and catches if a value is negative when not possible.

import random

def print_state(company, hours, rate, doc_num, gross):
    if(gross == -1):
        print("Invalid number of hours or pay rate.")
    else:
        print("\n\nCompany: {} \nhours: {} \nRate: ${:.2f} \n**********************************************\nYour "
              "document number is: {} \nYour {} gross pay is ${:.2f} dollars.".format(company, hours_float, rate_float, doc_num, company, gross))
    return 0

valid_hours = False
valid_rate = False
doc_num = random.randint(1000, 2000)
company = input("Enter your company name: ")
while(valid_hours == False):
    valid_hours = True
    hours = input("Enter the hours: ")
    try:
        hours_float = float(hours.strip())
    except ValueError:
        print("Error, please enter numeric input")
        valid_hours = False
while(valid_rate == False):
    valid_rate = True
    rate = input("Enter the rate: ")
    try:
        rate_float = float(rate.strip())
    except ValueError:
        print("Error, please enter numeric input")
        valid_rate = False

if(hours_float > 0 and hours_float <= 40 and rate_float >= 0):
    total_pay = hours_float * rate_float
elif (hours_float > 40 and rate_float >= 0):
    total_pay = (40 * rate_float) + ((hours_float - 40) * rate_float * 1.5)
else:
    total_pay = -1
print_state(company, hours_float, rate_float, doc_num, total_pay)
'''
Enter your company name: Apple
Enter the hours: 45
Enter the rate: 10


Company: Apple 
hours: 45.0 
Rate: $10.00 
**********************************************
Your document number is: 1527 
Your Apple gross pay is $475.00 dollars.

Enter your company name: Google
Enter the hours: Twenty
Error, please enter numeric input
Enter the hours: 20
Enter the rate: fourteen
Error, please enter numeric input
Enter the rate: 14


Company: Google 
hours: 20.0 
Rate: $14.00 
**********************************************
Your document number is: 1315 
Your Google gross pay is $280.00 dollars.

Enter your company name: Sony
Enter the hours: 100
Enter the rate: twelve
Error, please enter numeric input
Enter the rate: -12
Invalid number of hours or pay rate.
'''