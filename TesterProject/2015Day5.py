# pt 1
import re
import sys

if len(sys.argv) < 2:
    print("Usage: python 2015Day5.py <input filename>")
    exit(-1)

file = sys.argv[1]

txt_file = open(file)
vowels = "[aeiou]"
banned = ["ab", "cd", "pq", "xy"]

total_nice = 0

for line in txt_file:
    is_ban = False
    vowel_count = 0
    for ban in banned:
        if ban in line:
            is_ban = True
    has_double = re.search(r'(\w)\1', line)
    vowel_count = len(re.findall(vowels, line))
    if (not is_ban) and (has_double != None) and (vowel_count >= 3):
        total_nice += 1

# print(total_nice)
txt_file.close()
# answer: 255 nice strings(correct)

# pt 2
txt_file = open("2015Day5.txt")

def sandwich(line):
    return re.search(r'(.).\1', line)

def double_repeat(line):
    return re.search(r'(.)(.).*\1\2', line)

new_nice = 0

for line in txt_file:
    if double_repeat(line) and sandwich(line):
        new_nice += 1

print("".format(new_nice))
#answer: 55
