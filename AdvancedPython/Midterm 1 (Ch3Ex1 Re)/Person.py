import time
import datetime


class Person:
    def __init__(self):
        order = {}

    def TotalCharge(self):
        return

    def print_receipt(self, order, gross, tax):
        '''This function prints out the "receipt" for the order and returns it as a string'''
        receipt = ""
        receipt += "Your bill for today:\n--------------------\n"
        for i in order:
            if order[i][2] > 0:
                receipt += "[#{} {}:  ${}] x {}\n".format(i, order[i][0], order[i][1], order[i][2])
        receipt += "\nTotal before tax:   ${:.2f}\n\t\t\t Tax:   ${:.2f}\nTotal Price:\t\t${:.2f}".format(gross, tax,
                                                                                                          gross + tax)

        print(receipt)
        return receipt

    def SaveToFile(self, order, gross, tax):
        '''
        This function saves the same receipt as being printed out to file in the same directory
        as the script file.

        :param order: the order entered by the user
        :param gross: total price pre-tax
        :param tax: tax
        :return: null
        '''
        timeStamp = time.time()
        orderTimeStamp = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H-%M-%S')
        orderTimeStamp = orderTimeStamp + ".txt"

        receipt = self.print_receipt(order, gross, tax)

        with open(orderTimeStamp, 'w') as fileHandleToSaveTheBill:
            fileHandleToSaveTheBill.write(receipt)
        return
