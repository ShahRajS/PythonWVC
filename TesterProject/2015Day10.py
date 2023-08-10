import numpy
import re

def looksay(inp):
    newNum = 0
    newNum = re.sub(r'(\d)\1*', lambda x: str(len(x.group(0)))+x.group(1), str(inp))

    return newNum


input = 3113322113

for i in range(50):
    input = looksay(input)
print(len(input))