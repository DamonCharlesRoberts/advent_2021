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

df.loc[df['direction'] == 'forward', 'horizontal'] = df['magnitude']
df.loc[df['direction'] == 'up', 'depth'] = -df['magnitude']
df.loc[df['direction'] == 'down', 'depth'] = df['magnitude']
df.fillna(0)	
add = df.sum()
total = add['horizontal'] * add['depth']