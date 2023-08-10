from re import *

txt_list = ["Hello, Lads and Laddesses.", "Hello World", "Goodbye World", "Python is fun", "python is Fun"]
valid_list = []
for txt in txt_list:
    if search("^Hello.*Laddesses.$", txt) != None:
        valid_list.append(search("^Hello.*Laddesses.$", txt))

find_list = findall("^Hello.*Laddesses.$", txt)


#print(valid_list)
#print(find_list)

banned = ["ab", "cd", "pq", "xy"]
vow = ["a", "e", "i", "o", "u"]
str = "abcdefghijklmnopqrstuvwxyz"
strings = ["abcd", "acbd", "alpq", "avxy", "pyhw", "bhi", "qaw"]
for st in strings:
    for ban in banned:
        if ban in st:
            print("{} is in {}".format(ban, st))


for c in str:
    if c in vow:
        print(c)