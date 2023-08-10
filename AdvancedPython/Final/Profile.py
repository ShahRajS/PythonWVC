class Profile:
    def __init__(self, name="Default"):
        self.name = name
        self.friendsList = []
        self.network = []

    def get_name(self):
        return self.name

    def add_friend(self, friend_name):
        self.friendsList.append(friend_name)

    def remove_friend(self, friend_name):
        if (friend_name in self.friendsList):
            self.friendsList.remove(friend_name)
        else:
            print(friend_name + " is not in your friend's list.\n")

    def print_info(self):
        return "Name: " + self.name + "\nYour Friends: " + ', '.join(self.friendsList)
