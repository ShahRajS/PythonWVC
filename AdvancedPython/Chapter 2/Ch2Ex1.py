#Raj Shah
#CIST-005B-72148

#
from getInputsFile import getInputs
from computePayFile import computePay
from printPayFile import printPay

COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]
user = getInputs(COMPANYLIST)
gross_pay = computePay(user["hours"], user["rate"])
printPay(user["company_name"], user["hours"], user["rate"], gross_pay)

'''
Enter your company name: Google
Enter the hours: 65
Enter the rate: 20


Company: Google 
Hours: 65.0 
Rate: $20.00 
**********************************************
Your document number is: 1654 
Your Google gross pay is $1550.00 dollars.

Process finished with exit code 0

Enter your company name: Target
This is not an accepted company.
Enter your company name: Walmart
This is not an accepted company.
Valid companies:  ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
Enter your company name: West Valley
This is not an accepted company.
Valid companies:  ['Amazon', 'Apple', 'Facebook', 'Google', 'Uber']
Enter your company name: Google
Enter the hours: 
Error, please enter numeric input
Enter the hours: Twenty
Error, please enter numeric input
Enter the hours: 55
Enter the rate: sixteen
Error, please enter numeric input
Enter the rate: 16


Company: Google 
Hours: 55.0 
Rate: $16.00 
**********************************************
Your document number is: 1619 
Your Google gross pay is $1000.00 dollars.

Process finished with exit code 0
'''