import re
import sys

file = sys.argv[1]
#file = sys.argv[2]
txt_file = open(file)
instructions = []
for line in txt_file:
    sp = line.split()
    instructions.append(sp[0])

extra_ch = 0

for line in instructions:
    num_of_hex = len(re.findall(r'\\x[0-9, a-f][0-9, a-f]', line)) * 3
    extra_ch += num_of_hex
    num_of_quotes = len(re.findall(r'\"', line))
    extra_ch += num_of_quotes
    num_of_double = len(re.findall(r'(\\)\1', line))
    extra_ch += num_of_double

print("Total excess raw characters: " + str(extra_ch))

addons = 0

for line in instructions:
    num_of_hex = len(re.findall(r'\\x[0-9, a-f][0-9, a-f]', line))
    addons += num_of_hex
    num_of_quotes = len(re.findall(r'\"', line))
    addons += num_of_quotes * 2
    num_of_double = len(re.findall(r'(\\)\1', line))
    addons += num_of_double * 2

print(addons)