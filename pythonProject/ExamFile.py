import random

class Pet1:
    def __init__(self, name_str, type_str, weight_int):
        self.name = name_str
        self.type = type_str
        self.weight = weight_int
        self.hunger = 5
        self.milesTraveled = 0

    def walk(self, miles):
        if self.type == "dog":
            self.milesTraveled += miles
        else:
            print("you can't take your {} for a walk.".format(self.type))

    def feed(self):
        if self.hunger < 7:
            self.hunger -= 3
        else:
            print("{} isn't hungry right now...".format(self.name))

    def __str__(self):
        return "{} is a {} that weighs {}. {}'s hunger level is {}, and has walked {} miles today".format(self.name, self.type, self.weight, self.name, self.hunger, self.milesTraveled)

#lulu = Pet1("Lulu", "dog", 12)
#lulu.walk(10)
#lulu.feed()
#print(lulu)
#oliver = Pet1("Oliver", "cat", 8)
#oliver.walk(10)
#oliver.feed()
#print(oliver)

#-----------------------------------------------End problem 1-----------------------------------------------

class Recipe:
    def __init__(self, name_str, cals_float, ing_list, servings_int, time_int):
        self.name = name_str
        self.cals = cals_float
        self.ingredients = ing_list
        self.servings = servings_int
        self.time = time_int

    def serving_calories(self):
        return self.cals / self.servings

    def change_servings(self, new_serv):
        self.servings = new_serv

    def add_ingredient(self, new_ing):
        self.ingredients.append(new_ing)

    def remove_ingredient(self, ing):
        if ing in self.ingredients:
            self.ingredients.remove(ing)
        else:
            print("{} is not in the current ingredient list".format(ing))

    def __str__(self):
        return "{} has {} servings, {} calories, making it {} calories per serving. It contains {}, and takes {} minutes to cook.".format(self.name, self.servings, self.cals, self.serving_calories(), self.ingredients, self.time)


#soup = Recipe("vegetarian chili", 1200, ["chili powder", "cumin", "black beans", "pinto beans", "broth", "onions", "bell peppers"], 6, 30)
#print(soup)
#soup.add_ingredient("serrano peppers")
#soup.remove_ingredient("bell peppers")
#soup.change_servings(4)
#print(soup)

#-----------------------------------------End Prob 2--------------------------------------------------------

def pascals_triangle_var(rows):
    triangle = [[1], [1, 1]]
    for i in range(rows - 2):
        new_row = [1]
        for j in range(len(triangle[i + 1]) - 1):
            new_row.append(triangle[i + 1][j] + triangle[i + 1][j + 1] + triangle[i][j])
        new_row.append(1)
        triangle.append(new_row)

    for row in triangle:
        print(row)
pascals_triangle_var(5)

#----------------------------------------End Prob 5---------------------------------------------------------

class Pet:
    def __init__(self, name_str, age_int):
        self.name = name_str
        self.age = age_int
        self.visits = 0
        self.meds = []

    def visit(self):
        self.visits += 1

    def prescribed(self, med):
        self.meds.append(med)

class Dog(Pet):
    def __init__(self, name_str, age_int, legs_int = 4):
        super().__init__(name_str, age_int)
        self.legs = legs_int
    def __str__(self):
        return "{} is a {} year old dog who has visited the office {} times, and needs {}.".format(self.name, self.age, self.visits, self.meds)

class Bird(Pet):
    def __init__(self, name_str, age_int, legs_int = 2):
        super().__init__(name_str, age_int)
        self.legs = legs_int
    def __str__(self):
        return "{} is a {} year old bird who has visited the office {} times, and needs {}".format(self.name, self.age, self.visits, self.meds)

#gustavo = Bird("Gustavo", 5)
#lulu = Dog("Lulu", 12)
#gustavo.visit()
#gustavo.prescribed("Fish Oil Supplements")
#lulu.visit()
#lulu.prescribed("Fish Oil Supplements")
#print(gustavo)
#print(lulu)

#--------------------------------------------End Prob 6-----------------------------------------------------

def rand_names(first, last):
    webs = ["gmail", "yahoo", "hotmail", "myspace", "mywvm", "RIPClubPenguin", "GengarBestBoi"]
    rand_f = random.choice(first)
    rand_l = random.choice(last)
    rand_web = random.choice(webs)

    return "{} {}: {}{}@{}.com".format(rand_f, rand_l, rand_f, rand_l, rand_web)

#for i in range(10):
#    print(rand_names(first_list, last_list))

#---------------------------------------End Prob 7---------------------------------------------------------
email_list = ["sat", "sun", "sat"]
def num_emails(day):
    total = 0
    for email in email_list:
        if day in email:
            total += 1

    return total

#---------------------------------------End Prob 8---------------------------------------------------------

test1 = "The quick brown fox jumps over the lazy dog"
test2 = "abc"
def alphabet_check(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for let in str:
        if let in alphabet:
            alphabet.remove(let)
    if alphabet == []:
        return True
    else:
        return False

#print(alphabet_check(test1))
#print(alphabet_check(test2))

