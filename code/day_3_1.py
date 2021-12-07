# Title: Advent 2021 - Day 3, Part 1
# Notes:
	#* Description: Script for Day 3, Part 1 of Advent of Code 2021
# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
from collections import Counter
	#* Working Directory
os.chdir('/Users/damonroberts/Dropbox/personal/advent_2021')
	#* Dataframes
df = np.loadtxt('data/day_3.txt', delimiter = '/n', dtype = 'str')
# Description of variables
	#* gamma rate = common bit in corresponding position of all numbers - first integer 0 - 5, 1 - 7. Gamma rate is therefore 1 for first, gamma rate is 0 for second, gamma rate 1 for third and fourth, gamma rate 0 for 5th. the gamma rate is binary number 10110 or 22 in decimal
	#* epsilon rate = least common bit from each position 01001 or 9 in decimal
	#* power consumption = gamma * epsilon (9 x 22 = 198)
location = np.arange(0, 12, 1) #12 digit binary readings
gamma = []
epsilon = []
for i in location:
	count = Counter(t[i] for t in df) #get count of each integer at each location in the string
	diff = count['1'] - count['0'] # deterimine which integer is more common in each location
	if diff > 0:
		gbinary = '1'
	else:
		gbinary = '0'
	gamma.append(gbinary) # give me my gamma rate
	if diff > 0:
		ebinary = '0'
	else:
		ebinary = '1'
	epsilon.append(ebinary) # give me my epsilon rate

gbinary = ''.join(gamma) #join the lists
gbinary = int(gbinary) #convert it from string to integer
ebinary = ''.join(epsilon)#join the lists
ebinary = int(ebinary)#convert it from string to integer

# Define function to turn binary to decimal
def binaryToDecimal(binary):
	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
    	dec = binary % 10
    	decimal = decimal + dec * pow(2, i)
    	binary = binary//10
    	i += 1
	return decimal 

gdecimal = binaryToDecimal(gbinary)#get gamma rate decimal
edecimal = binaryToDecimal(ebinary)#get epsilon rate decimal

powerConsumption = gdecimal * edecimal#calculate powerconsumption