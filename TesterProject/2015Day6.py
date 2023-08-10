import re
import numpy as np

txt_file = open("2015Day6.txt")
#edit_file = txt_file.split("x")
str_txt = ""
for line in txt_file:
    str_txt += line
str_txt = str_txt.replace("through", "")
str_txt = str_txt.replace("turn", "")
edit_txt = str_txt.split("\n")
new_dirs = []
for words in edit_txt:
    if words != "":
        if words[0] == " ":
            words = words[1:]
        new_dirs.append(words)
finale = []
for word in new_dirs:
    words = re.split(" |,", word)
    words.remove("")
    finale.append(words)
print(finale)

lights = np.zeros((1000, 1000))

def set_light(config, x_1, y_1, x_2, y_2):
    for x in range(x_1, x_2 + 1):
        for y in range(y_1, y_2 + 1):
            if config == "off":
                lights[x][y] = 0
            elif config == "on":
                lights[x][y] = 1
            else:
                lights[x][y] = not lights[x][y]

for dirs in finale:
    x1 = int(dirs[1])
    y1 = int(dirs[2])
    x2 = int(dirs[3])
    y2 = int(dirs[4])
    set_light(dirs[0], x1, y1, x2, y2)
    #print("x1: {}, y1: {}, x2: {}, y2: {}".format(x1, y1, x2, y2))

total_on = 0
for i in range(1000):
    for j in range(1000):
        if lights[i][j] == 1:
            total_on += 1
print("Total number of lights on: {}".format(total_on))