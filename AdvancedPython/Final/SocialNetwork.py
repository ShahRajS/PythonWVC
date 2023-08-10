# Social main interface
from Profile import Profile
import random as r

existing_profile_names = ["Aditya", "Bethany", "Cho", "David", "Ella", "Farhan", "Gregori", "Hana", "Ivy", "Jaden"]
cist5b = {}
for names in existing_profile_names:
    cist5b[names] = Profile(names)

name = input("Enter your profile name: ")
user_acc = Profile(name)

if (int(input("Do you want to join the network? 1 for yes, 0 for no: "))):
    cist5b[user_acc.get_name()] = user_acc

print("Here are some of the people in this network: ")
for i in range(3):
    print(existing_profile_names[r.randrange(0, len(existing_profile_names))])

user_acc.add_friend(input("Enter a name to add them to your friend's list: "))
while (int(input("Do you want to add more friends? 1 for yes, 0 for no: "))):
    user_acc.add_friend(input("Enter a name to add them to your friend's list: "))

while (int(input("Do you want to remove any friends? 1 for yes, 0 for no: "))):
    non_friend = input("Enter a name in your friend's list to remove them: ")
    user_acc.remove_friend(non_friend)

print(user_acc.print_info())
