import re
import numpy as np

def count_status(status, board):
    total = 0
    for i in board:
        for j in i:
            if j == status:
                total += 1
    return total


def light_swap(lights):
    new_setup = lights
    for i in range(lights):
        for j in range(lights[0]):
            if i == 0:
                count_status("#", [[".", ".", "."], [lights[i][j - 1], lights[i][j], lights[i][j + 1]], [lights[i + 1][j - 1]], lights[i + 1][j], lights[i + 1][j + 1]])
    return new_setup

txt_file = open("2015Day18.txt")

off = "."
on = "#"

board = [] #board[row][column]
for line in txt_file:
    row = []
    for char in line:
        row.append(char)
    board.append(row)

for i in range(100):
    board = light_swap(board)

