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
        self.floor = 1
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
    def set_coords(self, set_x, set_y):
        self.x = set_x
        self.y = set_y
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
    def set_coords(self, set_x, set_y):
        self.x = set_x
        self.y = set_y
    def __str__(self):
        return "[💰]"
class Medkit:
    def __init__(self, name_str, x_int, y_int):
        self.name = name_str
        self.used = False
        self.heals = 10
        self.x = x_int
        self.y = y_int
    def set_coords(self, set_x, set_y):
        self.x = set_x
        self.y = set_y
    def __str__(self):
        return "[🩹]"

class Ladder:
    def __init__(self, x_int, y_int):
        self.x = x_int
        self.y = y_int
    def set_coords(self, set_x, set_y):
        self.x = set_x
        self.y = set_y
    def __str__(self):
        return "[🚪]"

class Trap:
    def __init__(self, x_int, y_int, damage_int):
        self.x = x_int
        self.y = y_int
        self.tripped = False
        self.damage = damage_int
    def set_coords(self, set_x, set_y):
        self.x = set_x
        self.y = set_y
    def __str__(self):
        if self.tripped:
            return "[💣]"
        else:
            return "[   ]"

def click():
    entered_text = textbox.get()
    Label(win, text="[   ]", bg=random.choice(cave_colors), fg="grey").grid(row=player1.x, column=player1.y)
    textbox.delete(0, END)
    output.delete(0.0, END)
    info_box.delete(0.0, END)
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
    Label(win, text = str(player1), bg=random.choice(cave_colors), fg="violet").grid(row=player1.x, column=player1.y)
    if player1.x == med.x and player1.y == med.y and med.used == False:
        player1.change_hp(med.heals)
        med.used = True
        text += "You found medicine! Healed by {}.".format(med.heals)
    if player1.x == ladder.x and player1.y == ladder.y:
        text += "You found a ladder! Going to the next floor."
        game_setter(ladder.x, ladder.y)
        player1.floor += 1
    for trap in trap_list:
        if player1.x == trap.x and player1.y == trap.y:
            player1.change_hp(-1 * trap.damage)
            trap.tripped = True
            text += "You landed on a trap! Lost {} HP.".format(trap.damage)
    for gold in treasure_list:
        if player1.x == gold.x and player1.y == gold.y and gold.used == False:
            player1.add_money(gold)
            gold.used = True
            text += "You found {} gold! Added to your wallet\n".format(gold.value)
    output.insert(END, text)
    info_txt = "Current floor: {}\nCurrent score: {:.3f}\n Wallet: {}\n Current HP: {}".format(player1.floor, player1.score(), player1.money, player1.HP)
    info_box.insert(END, info_txt)
    if player1.HP == 0:
        print("You ran out of HP and died :(\n")
        exitter()

def exitter():
    print("Total treasure: {}\n Final HP: {}\n Final Score: {}".format(player1.money, player1.HP, player1.score()))
    quit()

def game_setter(p_x = 4, p_y = 4):
    for w in range(width_set):
        for l in range(length_set):
            Label(win, text="[   ]", bg=random.choice(cave_colors), fg="tan").grid(row=l, column=w)

    for i in range((width_set * length_set) // 16):
        rand_x = random.randrange(0, width_set)
        rand_y = random.randrange(0, length_set)
        tre = Treasure("Gold", random.randint(1, 20), rand_x, rand_y)
        treasure_list.append(tre)
        Label(win, text=str(tre), bg=random.choice(cave_colors), fg="gold").grid(row=rand_x, column=rand_y)

    for i in range((width_set * length_set) // 20):
        rand_x = random.randrange(0, width_set)
        rand_y = random.randrange(0, length_set)
        rand_dmg = random.randint(5, 15)
        trap = Trap(rand_x, rand_y, rand_dmg)
        trap_list.append(trap)
        Label(win, text=str(trap), bg=random.choice(cave_colors), fg="tan").grid(row=rand_x, column=rand_y)

    med_x = random.randrange(0, width_set)
    med_y = random.randrange(0, length_set)
    med.set_coords(med_x, med_y)
    Label(win, text=str(med), bg=random.choice(cave_colors), fg="green").grid(row=med_x, column=med_y)

    lad_x = random.randrange(0, width_set)
    lad_y = random.randrange(0, length_set)
    ladder.set_coords(lad_x, lad_y)
    Label(win, text=str(ladder), bg=random.choice(cave_colors), fg="black").grid(row=lad_x, column=lad_y)

    player1.set_coords(p_x, p_y)
    Label(win, text=str(player1), bg=random.choice(cave_colors), fg="violet").grid(row=player1.x, column=player1.y)
#---------------------------------------------------------
player1 = Player("Blobby")
rules_txt = "Movement:\nW: Forward⬆\nA: Left⬅\nS: Backward⬇\nD: Right➡"
cave_colors = ["lightsalmon4", "salmon4", "tomato4", "coral4", "sienna4"]
med = Medkit("Bandage", 0, 0)
ladder = Ladder(0, 0)
treasure_list = []
trap_list = []

win = Tk()
win.title("Dungeon Crawlhalla Map")
win.configure(background = "tan")

width_set = 10
length_set = 10

game_setter()

Button(win, text = "Exit", width = 6, command = exitter).grid(row = 0, column = width_set, sticky = NE)
Button(win, text = "Start Over", width = 9, command = game_setter).grid(row = 0, column = width_set, sticky = NW)

textbox = Entry(win, width = 23, bg = "lightsteelblue2")
textbox.grid(row = length_set, column = 0, columnspan = 10, sticky = W)
Button(win, text = "Submit", width = 8, command = click).grid(row = length_set, column = 6, columnspan = 3, sticky = W)
output = Text(win, width = 26, height = 6, wrap = WORD, background = "silver")
output.grid(row = length_set+1,column = 0, columnspan = 10, sticky = NW)
rules_box = Text(win, width = 15, height = 10, wrap = WORD, background = "silver")
rules_box.grid(row = 0, column = length_set, rowspan = 10)
rules_box.insert(END, rules_txt)

info_box = Text(win, width = 15, height = 7, wrap = WORD, background = "gold")
info_box.grid(row = 7, column = length_set, rowspan = 10)

win.mainloop()