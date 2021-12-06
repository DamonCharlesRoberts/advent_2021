# Title: Advent 2021 - Day 1, Part I
# Notes:
	#* Description: Script for Day 1, Part I of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
	#* Working Directory
os.chdir('/Users/damonroberts/Dropbox/personal/advent_2021')
	#* Dataframes
df = np.loadtxt('data/day_1.txt', delimiter='\n', dtype=int)
diff = []
# Solution
	#* Subtract current list item from previous list item
for i in range(1,len(df)):
    x = df[i] - df[i-1]
    diff.append(x)
    #* Get count of positive numbers
pos_count = len(list(filter(lambda x: (x >= 0), diff)))