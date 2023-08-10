#Raj Shah
#CIST-005B-72148

#This program has a dictionary of friends you made in 2017 and 2018. It then checks if a friend
#you inputted was made in 2017 or 2018, or a different year. It then adds a new friend you made in
#2017 or 2018, and adds them to dictionary and presents both sets of friends.

friends = {"2017": ["Gideon", "Jeffrey", "Rad"], "2018": ['Sanya', 'Christine', 'Evan']}
print("Your friends: {} {}".format(friends["2017"], friends["2018"]))
curr_friend = input("Enter a name of a friend: ")
if curr_friend in friends["2017"]:
    print("You met {} in 2017!".format(curr_friend))
elif curr_friend in friends["2018"]:
    print("You met {} in 2018".format(curr_friend))
else:
    print("You didn't meet this friend in 2017 or 2018")
new_friend = input("Enter the name of another friend you made in 2017 or 2018: ")
new_fr_yr = int(input("What year did you meet this friend? "))
if new_fr_yr == 2017:
    friends["2017"].append(new_friend)
else:
    friends["2018"].append(new_friend)
print("Friends met in 2017: {}\nFriends met in 2018: {}".format(friends["2017"], friends["2018"]))

'''
Your friends: ['Gideon', 'Jeffrey', 'Rad'] ['Sanya', 'Christine', 'Evan']
Enter a name of a friend: Rad
You met Rad in 2017!
Enter the name of another friend you made in 2017 or 2018: Johnny
What year did you meet this friend? 2018
Friends met in 2017: ['Gideon', 'Jeffrey', 'Rad']
Friends met in 2018: ['Sanya', 'Christine', 'Evan', 'Johnny']

Your friends: ['Gideon', 'Jeffrey', 'Rad'] ['Sanya', 'Christine', 'Evan']
Enter a name of a friend: Sanya
You met Sanya in 2018
Enter the name of another friend you made in 2017 or 2018: Boban
What year did you meet this friend? 2018
Friends met in 2017: ['Gideon', 'Jeffrey', 'Rad']
Friends met in 2018: ['Sanya', 'Christine', 'Evan', 'Boban']
'''