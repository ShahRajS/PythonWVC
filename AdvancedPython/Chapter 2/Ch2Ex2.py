#Raj Shah
#CIST-005B-72148

#This program has a list of friends you made in 2017 and 2018. It then checks if a friend
#you inputted was made in 2017 or 2018, or a different year. It then adds a new friend you made in
#2017 or 2018, and adds them to the list and presents both lists of friends.

friends_2017 = ["Gideon", "Jeffrey", "Rad"]
friends_2018 = ["Sanya", "Christine", "Evan"]
print("Your friends:",friends_2017 + friends_2018)
curr_friend = input("Enter a name of a friend: ")
if curr_friend in friends_2017:
    print("You met {} in 2017!".format(curr_friend))
elif curr_friend in friends_2018:
    print("You met {} in 2018".format(curr_friend))
else:
    print("You didn't meet this friend in 2017 or 2018")
new_friend = input("Enter the name of another friend you made in 2017 or 2018: ")
new_fr_yr = int(input("What year did you meet this friend? "))
if new_fr_yr == 2017:
    friends_2017.append(new_friend)
else:
    friends_2018.append(new_friend)
print("Friends met in 2017: {}\nFriends met in 2018: {}".format(friends_2017, friends_2018))

'''
Your friends: ['Gideon', 'Jeffrey', 'Rad', 'Sanya', 'Christine', 'Evan']
Enter a name of a friend: Rad
You met Rad in 2017!
Enter the name of another friend you made in 2017 or 2018: Bhatt
What year did you meet this friend? 2017
Friends met in 2017: ['Gideon', 'Jeffrey', 'Rad', 'Bhatt']
Friends met in 2018: ['Sanya', 'Christine', 'Evan']

Your friends: ['Gideon', 'Jeffrey', 'Rad', 'Sanya', 'Christine', 'Evan']
Enter a name of a friend: Joseph
You didn't meet this friend in 2017 or 2018
Enter the name of another friend you made in 2017 or 2018: Brad
What year did you meet this friend? 2018
Friends met in 2017: ['Gideon', 'Jeffrey', 'Rad']
Friends met in 2018: ['Sanya', 'Christine', 'Evan', 'Brad']
'''