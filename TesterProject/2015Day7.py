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
    split.remove("->")
    instructions.append(split)
print(instructions)