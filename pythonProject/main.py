from tkinter import *
import random

class Player:
    def __init__(self, name_str):
        self.name = name_str
        self.max_HP = 100
        self.HP = 100
        self.money = 0
        self.x = 4
        self.y = 4
    def change_hp(self, dmg):
        self.HP += dmg
        if self.HP > 100:
            self.HP = 100
        elif self.HP < 0:
            self.HP = 0
    def move(self, y_mov, x_mov):
        self.x += x_mov
        self.y += y_mov
    def add_money(self, treasure):
        self.money += treasure.value
    def score(self):
        if self.HP > 0 and self.HP != self.max_HP:
            return ((self.money * 50) / (self.max_HP - self.HP))
        elif self.HP == self.max_HP:
            return (self.money * 100)
        else:
            return 0
    def __str__(self):
        return "[🤠‍]"

class Treasure:
    def __init__(self, name_str, value_int, x_int, y_int):
        self.used = False
        self.name = name_str
        self.value = value_int
        self.x = x_int
        self.y = y_int
    def __str__(self):
        return "[💰]"
class Medkit:
    def __init__(self, name_str, x_int, y_int):
        self.name = name_str
        self.used = False
        self.heals = 10
        self.x = x_int
        self.y = y_int
    def __str__(self):
        return "[🩹]"

class Ladder:
    def __init__(self, x_int, y_int):
        self.x = x_int
        self.y = y_int
    def __str__(self):
        return "[🚪]"

def click():
    entered_text = textbox.get()
    Label(win, text="[   ]", bg=random.choice(cave_colors), fg="black").grid(row=player1.x, column=player1.y)
    textbox.delete(0, END)
    output.delete(0.0, END)
    if entered_text == "W" or entered_text == "w" and player1.x > 0:
        text = "You moved forward."
        player1.move(0, -1)
    elif entered_text == "S" or entered_text == "s" and player1.x < (width_set - 1):
        text = "You moved back."
        player1.move(0, 1)
    elif entered_text == "A" or entered_text == "a" and player1.y > 0:
        text = "You moved left."
        player1.move(-1, 0)
    elif entered_text == "D" or entered_text == "d" and player1.y < (length_set - 1):
        text = "You moved right."
        player1.move(1, 0)
    else:
        text = "Invalid movement, try again."
        player1.HP += 1
    player1.HP -= 1
    Label(win, text = str(player1), bg=random.choice(cave_colors), fg="black").grid(row=player1.x, column=player1.y)
    if player1.x == med.x and player1.y == med.y and med.used == False:
        player1.change_hp(med.heals)
        med.used = True
        text += "You found medicine! Healed by {}...".format(med.heals)
    elif player1.x == ladder.x and player1.y == ladder.y:
        text += "You found a ladder! Going to the next floor..."
    for gold in treasure_list:
        if player1.x == gold.x and player1.y == gold.y and gold.used == False:
            player1.add_money(gold)
            gold.used = True
            text += "You found {} gold! Added to your bag...\n".format(gold.value)

    text += " You have {} gold and you have {} HP.".format(player1.money, player1.HP)
    output.insert(END, text)
    if player1.HP == 0:
        print("You ran out of HP and died :(\n")
        exitter()

def exitter():
    print("Total treasure: {}\n Final HP: {}\n Final Score: {}".format(player1.money, player1.HP, player1.score()))
    quit()
#---------------------------------------------------------
player1 = Player("Blobby")
rules_txt = "Movement:\nW: Forward⬆\nA: Left⬅\nS: Backward⬇\nD: Right➡"
cave_colors = ["lightsalmon4", "salmon4", "tomato4", "coral4", "sienna4"]

win = Tk()
win.title("Dungeon Crawlhalla Map")
win.configure(background = "tan")

width_set = 10
length_set = 10
treasure_list = []

for w in range(width_set):
    for l in range(length_set):
        Label(win, text = "[   ]", bg=random.choice(cave_colors), fg = "black").grid(row=l, column=w)

for i in range((width_set * length_set) // 16):
    rand_x = random.randrange(0, width_set)
    rand_y = random.randrange(0, length_set)
    tre = Treasure("Gold", random.randint(1, 20), rand_x, rand_y)
    treasure_list.append(tre)
    Label(win, text=str(tre), bg=random.choice(cave_colors), fg="black").grid(row=rand_x, column=rand_y)

med_x = random.randrange(0, width_set)
med_y = random.randrange(0, length_set)
med = Medkit("Bandage", med_x, med_y)
Label(win, text=str(med), bg=random.choice(cave_colors), fg="black").grid(row=med_x, column=med_y)

lad_x = random.randrange(0, width_set)
lad_y = random.randrange(0, length_set)
ladder = Ladder(lad_x, lad_y)
Label(win, text=str(ladder), bg=random.choice(cave_colors), fg="black").grid(row=lad_x, column=lad_y)

Button(win, text = "Exit", width = 6, command = exitter).grid(row = 0, column = width_set, sticky = NE)
Label(win, text = str(player1), bg="lightsalmon4", fg = "black").grid(row=player1.x, column=player1.y)
textbox = Entry(win, width = 23, bg = "lightsteelblue2")
textbox.grid(row = length_set, column = 0, columnspan = 10, sticky = W)
Button(win, text = "Submit", width = 8, command = click).grid(row = length_set, column = 6, columnspan = 3, sticky = W)
output = Text(win, width = 26, height = 6, wrap = WORD, background = "grey")
output.grid(row = length_set+1,column = 0, columnspan = 10, sticky = NW)
rules_box = Text(win, width = 15, height = 10, wrap = WORD, background = "silver")
rules_box.grid(row = 0, column = length_set, rowspan = 10)
rules_box.insert(END, rules_txt)

win.mainloop()