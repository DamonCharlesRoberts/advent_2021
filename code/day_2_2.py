# Title: Advent 2021 - Day 2, Part 2
# Notes:
	#* Description: Script for Day 2, Part 2 of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
	#* Working Directory
os.chdir('/Users/damonroberts/Dropbox/personal/advent_2021')
	#* Dataframes
df = pd.read_csv('data/day_2.txt', sep = ' ', names = ['direction', 'magnitude'])

# Calculate horizontal change
df.loc[df['direction'] == 'forward', 'horizontal'] = df['magnitude'] 
# Calculate depth change
df.loc[df['direction'] == 'up', 'depth'] = -df['magnitude']
df.loc[df['direction'] == 'down', 'depth'] = df['magnitude']
# Calculate aim
df.loc[df['direction'] == 'up', 'aim'] = -df['magnitude']
df.loc[df['direction'] == 'down', 'aim'] = df['magnitude']

df = df.fillna(0)
for i in range(1,len(df)):
	df.loc[i, 'totalhorizontal'] = df.loc[i-1, 'horizontal'] + df.loc[i, 'horizontal']
	df.loc[i, 'aim'] = df.loc[i-1, 'aim'] + df.loc[i, 'aim']
	if df.loc[i, 'direction'] == 'forward':
		df.loc[i, 'totaldepth'] = df.loc[i-1, 'aim'] * df.loc[i, 'magnitude']
	else: 
		df.loc[i, 'totaldepth'] = 0
# Add columns to get total horizontal and depth position
add = df.sum()
# Get total position by multiplying horizontal and depth change
total = add['horizontal'] * add['totaldepth']