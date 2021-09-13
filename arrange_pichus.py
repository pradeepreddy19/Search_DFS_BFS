#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : Pradeep Reddy Rokkam, prokkam@iu.edu, UID :2000766513
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    print(row,col,"Pradeep")
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) 
    if house_map[r][c] == '.' and ("p" not in house_map[r] ) and ("p" not in [row[c] for row in house_map]) 
     and ("p" not in [house_map[i][j] for i,j in diagonal_squares(house_map,r,c) ] ) ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Get all sqaures tha are diagonal to the given cell 
def diagonal_squares(house_map,r,c):
    i=0
    row=r
    col=c
    diag_elements=[]
    while i<len(house_map):
        a=row-i
        print(i)
        if i< row:
            if  row-a>=0  and col-a>=0:
                diag_elements.append((row-a,col-a))
            if   row-a>=0  and col+a<len(house_map[0]):
                diag_elements.append((row-a,col+a))
        a=i-row
        if i>row:
            if  row+a<len(house_map)  and col-a>=0:
                diag_elements.append((row+a,col-a))
            if   row+a<len(house_map)  and col+a<len(house_map[0]):
                diag_elements.append((row+a,col+a))
        i+=1
    return diag_elements

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#
def solve(initial_house_map,k):
    fringe = [initial_house_map]
    
    while len(fringe) > 0:
        # print("Pradeep Reddy Rokkam")
        # print(fringe)
        for new_house_map in successors( fringe.pop() ):
            print(printable_house_map(new_house_map))
            print("|*|"*50)
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)

# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")


