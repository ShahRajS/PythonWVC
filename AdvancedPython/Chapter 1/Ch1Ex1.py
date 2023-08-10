#Raj Shah
#CIST-005B-72148
#This program take an input of hours and pay rate, and computes the total amount owed
#calculating for overtime past 40 hours at a 1.5x rate to inputted rate


hours = int(input("Enter Hours: "))
rate = int(input("Enter Hourly Rate: "))
total_pay = 0;
if(hours > 0 and hours <= 40 and rate >= 0):
    total_pay = hours * rate
elif (hours > 40 and rate >= 0):
    total_pay = (40 * rate) + ((hours-40) * rate * 1.5)
else:
    print("Invalid number of hours or pay rate.")
    total_pay = -1
print("Pay:", total_pay)

'''
Enter Hours: 45
Enter Hourly Rate: 10
Pay: 475.0

Enter Hours: 60
Enter Hourly Rate: 10
Pay: 700.0
'''