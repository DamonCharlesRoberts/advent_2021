# Title: Advent 2021 - Day 3, Part 2
# Notes:
	#* Description: Script for Day 3, Part 2 of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import os
	#* Working Directory
os.chdir('/home/damoncroberts/Dropbox/personal/advent_2021')

	#* Dataframes
df = open('data/day_4.txt').read()
call, board = df.split('\n', 1)

# Make call array
call = [int(i) for i in call.split(',')]

# Make board array
board = board.strip().split('\n\n')
board = [np.array([[int(j) for j in i.split(' ') if j != ''] for i in board.strip().split('\n')]) for board in board]

def checkIfWon(board):
    for y in range(board.shape[0]):
        if np.all(board[y,:] < 0): return True
    for x in range(board.shape[1]):
        if np.all(board[:,x] < 0): return True
    return False

def result(board, num):
    return np.sum(board[board > 0]) * num

won = []
for num in call:
    for i in range(len(board) - 1, -1, -1):
        b = board[i]
        b[b == num] *= -1
        if checkIfWon(b):
            won.append((b, num))
            board.pop(i)

print('Part 1:' , result(*won[0]))
print('Part 2:' , result(*won[-1]))