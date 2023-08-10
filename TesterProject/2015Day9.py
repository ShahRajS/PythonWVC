import sys
import re

if len(sys.argv) < 2:
    print("Usage: python 2015Day7.py <input filename>")
    exit(-1)
file = sys.argv[1]
txt_file = open(file)
instructions = []
for line in txt_file:
    split = line.split()
    split.remove("to")
    split.remove("=")
    instructions.append(split)
    instructions.append([split[1], split[0], split[2]])
instructions.sort()
print(instructions)
departures = []
arrivals = []
for word in instructions:
    if word[0] not in departures:
        departures.append(word[0])
        arrivals.append(word[0])
shortest_len = sys.maxsize
for i in range(len(departures) ** 2):
    print(i)

