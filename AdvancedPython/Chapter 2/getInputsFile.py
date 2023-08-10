def getInputs(company_list):
    valid_company = 0
    valid_hours = False
    valid_rate = False
    while (valid_company >= 0):
        if valid_company >= 2:
            print("Valid companies: ", company_list)
        company = input("Enter your company name: ")
        if company in company_list:
            valid_company = -1
        else:
            print("This is not an accepted company.")
            valid_company += 1
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
    user_info = {"rate" : rate_float, "hours" : hours_float, "company_name" : company}
    return user_info