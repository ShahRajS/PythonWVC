import random
def printPay(company, hours, rate, gross):
    if(gross == -1):
        print("Invalid number of hours or pay rate.")
    else:
        print("\n\nCompany: {} \nHours: {} \nRate: ${:.2f} \n**********************************************\nYour "
              "document number is: {} \nYour {} gross pay is ${:.2f} dollars.".format(company, hours, rate, random.randint(1000, 2000), company, gross))
    return 0
