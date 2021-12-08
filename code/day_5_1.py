# Title: Advent of Code Day 5, Part 1

# Notes:
	#* Description: Script for Advent of Code Day 5, Part 1

# Setup
	#* Load Libraries
import numpy as np
import pandas as pd
import os
	#* Set working directory

os.chdir('/home/damoncroberts/Dropbox/personal/advent_2021')

	#* Load input

df = open('data/day_5_short.txt').read()

df = df.split('\n')
df = pd.DataFrame(df)
df = df[0].str.split('->', n = 1, expand = True)

new= df[0].str.split(',', n = 1, expand = True)
x1 = new[0]
x1 = [int(i) for i in x1]
y1 = new[1]
y1 = [int(i) for i in y1]

new = df[1].str.split(',', n = 1, expand = True)
x2 = new[0]
x2 = [int(i) for i in x2]
y2 = new[1]
y2 = [int(i) for i in y2]

def config_lists(x1, y1, x2, y2):
	line1 = list(zip(x1, y1))
	line2 = list(zip(x2, y2))
	return line1, line2
line1, line2 = config_lists(x1,y1,x2,y2)

test_tup = [(0,0), (0,1), (0,2), (0,3), (0, 4), (0,5), (0, 6), (0, 7), (0,8), (0,9), (1,0), (1,1), (1,2), (1,3), (1, 4), (1,5), (1, 6), (1, 7), (1,8), (1,9), (2,0), (2,1), (2,2), (2,3), (2, 4), (2,5), (2, 6), (2, 7), (2,8), (2,9), (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3, 7), (3,8), (3,9), (4,0), (4,1), (4,2), (4,3), (4, 4), (4,5), (4, 6), (4, 7), (4,8), (4,9), (5,0), (5,1), (5,2), (5,3), (5, 4), (5,5), (5, 6), (5, 7), (5,8), (5,9), (6,0), (6,1), (6,2), (6,3), (6, 4), (6,5), (6, 6), (6, 7), (6,8), (6,9), (7,0), (7,1), (7,2), (7,3), (7, 4), (7,5), (7, 6), (7, 7), (7,8), (7,9), (8,0), (8,1), (8,2), (8,3), (8, 4), (8,5), (8, 6), (8, 7), (8,8), (8,9), (9,0), (9,1), (9,2), (9,3), (9, 4), (9,5), (9, 6), (9, 7), (9,8), (9,9)]
test_tup = (0,0)
horizontal = []
horizontaltesttuple = [i[0] for i in test_tup]
def horizon(line1, horizontaltesttuple):
	for tup in line1:
		for i in horizontaltesttuple:
    		if(tup[1]>= horizontaltesttuple[i] and tup[0]<= horizontaltesttuple):
        		horizontal.append(tup)
horizon(line1, horizontaltesttuple)
vertical = []
for tup in line2:
	if(tup[1]>= test_tup[0] and tup[0]<= test_tup[1]):
		vertical.append(tup)

#def lSegInt(s1, s2, t1, t2):
#    if s1[0] != s2[0]:                # if s is not vertical
#        b1 = (s2[1] - s1[1])/float(s2[0] - s1[0])
#        if t1[0] != t2[0]:             # if t is not vertical
#            b2 = (t2[1] - t1[1]) / float(t2[0] - t1[0])
#            a1 = s1[1] - (b1 * s1[0])
#            a2 = t1[1] - (b2 * t1[0])
#            if b1 == b2:                # if lines are parallel (slopes match)
#                return(None)
#            xi = -(a1-a2)/float(b1-b2)  # solve for intersection point
#            yi = a1 + (b1 * xi)
#        else:
#            xi = t1[0]
#            a1 = s1[1] - (b1 * s1[0])
#            yi = a1 + (b1 * xi)
#    else:
#        xi = s1[0]
#        if t1[0] != t2[0]:            # if t is not vertical
#            b2 = (t2[1] - t1[1]) / float(t2[0] - t1[0])
#            a2 = t1[1] - (b2 * t1[0])
#            yi = a2 + (b2 * xi)
#        else:
#            return(None)
#    # Here is the actual intersection test!
#    if (s1[0]-xi)*(xi-s2[0]) >= 0 and \
#    (s1[1]-yi)*(yi-s2[1]) >= 0 and \
#    (t1[0]-xi)*(xi-t2[0]) >= 0 and \
#    (t1[1]-yi)*(yi-t2[1]) >= 0:
#        return((float(xi), float(yi)))  # Return the intersection point.
#    else:
#        return(None)
#
#
#def count_intersections(line1, line2):
##     Make sure the x values of both lines are same length and aligned.
#    intersections= 0
#    for i in range(len(line1) - 1):
##         Taking starting and end point of every segment in the line
#        x1_start, y1_start = line1[i]
#        x1_end, y1_end = line1[i + 1]
#        x2_start, y2_start = line2[i]
#        x2_end, y2_end = line2[i + 1]
#        if lSegInt([x1_start, y1_start], [x1_end, y1_end], [x2_start, y2_start], [x2_end, y2_end]):
#            intersections+= 1
#    return intersections

#print(count_intersections(line1, line2))

