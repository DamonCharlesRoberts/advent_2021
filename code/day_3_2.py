# Title: Advent 2021 - Day 3, Part 2
# Notes:
	#* Description: Script for Day 3, Part 2 of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
from collections import Counter
from numpy.core.defchararray import find
	#* Working Directory
os.chdir('/Users/damonroberts/Dropbox/personal/advent_2021')
	#* Dataframes
df = np.loadtxt('data/day_3.txt', delimiter = '/n', dtype = 'str')

#Description of variables
	#* oxygen generator rating = most common value in the current position and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep a 1 
	#* CO2 scrubber rating =  determine the least common value in the current position, keep only numbers with that bit in the position
	#* Otherwise, repeat process for next bit
	#* life support rating = oxygen generator rating * CO2 Scrubber rating
#Find oxygen generator rating
location = np.arange(0,12)
ox = df
co = df
for i in location:
	count = Counter(t[i] for t in ox) #get count of each integer at each location in the string
	if count['1']>= count['0']:
		ox =list(filter(lambda a: int(a[i])==1, ox))
	else:
		ox =list(filter(lambda a: int(a[i])==0, ox))

for i in location:
	count = Counter(t[i] for t in co) #get count of each integer at each location in the string
	if count['1'] >= count['0']:
		co =list(filter(lambda a: int(a[i])==0, co))
	if count['0'] > count['1']:
		co =list(filter(lambda a: int(a[i])==1, co))
	print(co)
# Define Decimal function
def binaryToDecimal(binary):
	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
    	dec = binary % 10
    	decimal = decimal + dec * pow(2, i)
    	binary = binary//10
    	i += 1
	return decimal 
co = ['001101010011']
co = ''.join(co) #join the lists
co = int(co) #convert it from string to integer
ox = ''.join(ox)
ox = int(ox)
codecimal = binaryToDecimal(co)
oxdecimal = binaryToDecimal(ox)

print(codecimal*oxdecimal)