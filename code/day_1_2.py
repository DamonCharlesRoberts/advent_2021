# Title: Advent 2021 - Day 1, Part 2
# Notes:
	#* Description: Script for Day 2, Part I of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
	#* Working Directory
os.chdir('/Users/damonroberts/Dropbox/personal/advent_2021')
	#* Dataframes
df = np.loadtxt('data/day_1.txt', delimiter='\n', dtype=int)
add = []
diff = []

#* Addition 3-measure window
for i in range(2,len(df)):
	x = df[i] + df[i-1] + df[i-2]
	add.append(x)
for i in range(1,len(add)):
    x = add[i] - add[i-1]
    diff.append(x)
pos_count = len(list(filter(lambda x: (x > 0), diff)))