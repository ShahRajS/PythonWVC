import hashlib
import re

def md5_checker(input_str, num_0):
    x = 1
    check = "0" * num_0
    while x > 0:
        key = input_str + str(x)
        value = hashlib.md5(key.encode())
        if str(value.hexdigest()[0:(num_0)]) == check:
            return x
        x += 1

print("First instance of {} zeros in the md5 hash is: {}".format(6, md5_checker("bgvyzdsv", 6)))