# Title: Advent 2021 - Day 2, Part I
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
df = pd.read_csv('data/day_2.txt', sep = ' ', names = ['direction', 'magnitude'])
# Calculate horizontal change
df.loc[df['direction'] == 'forward', 'horizontal'] = df['magnitude']
# Calculate depth change
df.loc[df['direction'] == 'up', 'depth'] = -df['magnitude']
df.loc[df['direction'] == 'down', 'depth'] = df['magnitude']
# Get rid of NAN
df.fillna(0)	
# Add columns to get total horizontal and depth position
add = df.sum()
# Get total position by multiplying horizontal and depth change
total = add['horizontal'] * add['depth']