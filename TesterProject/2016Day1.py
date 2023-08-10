#pt1

directions = "L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"
#directions = "R4, R4, R4"
merge_dir = directions.split(", ")

order = {0: 0, 1: 0, 2: 0, 3: 0}
curr_dir = 0

for dir in merge_dir:
    if dir[0] == "L":
        curr_dir -= 1
        if curr_dir < 0:
            curr_dir = 3
    elif dir[0] == "R":
        curr_dir += 1
        curr_dir = curr_dir % 4
    temp = dir[1:]
    for i in range(int(temp)):
        order[curr_dir] = order[curr_dir] + 1

print(order)
tot_blocks = abs(order[0] - order[2]) + abs(order[1] - order[3])
print(tot_blocks)
#answer: 273 blocks(correct)!

#pt2
blocks = {"0,0": 1}
x = 0
y = 0
curr_dir = 0

for dir in merge_dir:
    if dir[0] == "L":
        curr_dir -= 1
        if curr_dir < 0:
            curr_dir = 3
    elif dir[0] == "R":
        curr_dir += 1
        curr_dir = curr_dir % 4
    temp = dir[1:]
    for i in range(int(temp)):
        if curr_dir == 0:
            y += 1
        elif curr_dir == 1:
            x += 1
        elif curr_dir == 2:
            y -= 1
        else:
            x -= 1
        loc = str(x) + "," + str(y)
        if loc in blocks:
            print("total blocks: {}".format(abs(x) + abs(y)))
            exit(0)
        blocks[loc] = blocks.get(loc, 0) + 1
print("No intersection!")
#answer: 115 blocks(correct)
