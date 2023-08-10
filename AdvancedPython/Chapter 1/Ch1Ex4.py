#Raj Shah
#CIST-005B-72148
#This program take an input of an email and checks if it is valid, and prints out the domain name if so

email = input("Enter your email: ")
if ("@" in email and "." in email):
    print("The domain name of your email is", (email[email.index('@') + 1 : email.index('.')]))
else:
    print("This is not recognized as an email.")

'''
Enter your email: anonymous@gmail.com
The domain name of your email is gmail

Enter your email: anonymous@gmailcom
This is not recognized as an email.
'''