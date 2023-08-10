def computePay(hours, rate):
    if (hours > 0 and hours <= 40 and rate >= 0):
        total_pay = hours * rate
    elif (hours > 40 and rate >= 0):
        total_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        total_pay = -1
    return total_pay