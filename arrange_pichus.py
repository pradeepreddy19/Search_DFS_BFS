# !/usr/local/bin/python3

# arrange_pichus.py : arrange agents on a grid, avoiding conflicts

# Submitted by : Pradeep Reddy Rokkam, prokkam@iu.edu, UID :2000766513

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
    # print(row,col,"Pradeep")
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# Get list of successors of given house_map state
# def successors(house_map):
#     return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) 
#     if house_map[r][c] == '.' and ("p" not in house_map[r] ) and ("p" not in [row[c] for row in house_map]) 
#      and ("p" not in [house_map[i][j] for i,j in diagonal_squares(house_map,r,c) ] ) ]

# Slight modification to the scuccessor function to check whether a given sqaure is a legal square or not,


def successors(house_map):
    # print([ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) 
    # if house_map[r][c] == '.' and legal_square(house_map,r,c) ])
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) 
    if house_map[r][c] == '.' and legal_square(house_map,r,c) ]

# A slight modificaation to the successor function which will give return only the first housemap once we can 
# fit in the pichu in map
# Note: However this could not be the best legal square a pichu can be placed, however we will arrive the 
#      solution in faster way

# def successors(house_map):


#     # print([ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) 
#     # if house_map[r][c] == '.' and legal_square(house_map,r,c) ])

#     # The older code gives all possible successors where a pichu can be placed at for the given map.
#     # However, the following code breaks out of the loop and will return only one sucessor map where a pichu can 
#     # be placed at for the given map
#     for r in range(0, len(house_map)):
#         for c in range(0,len(house_map[0])):
#             if house_map[r][c] == '.' and legal_square(house_map,r,c):
#                 return [add_pichu(house_map, r, c)]
#     return []


#Return if a given square  of the given map is a legal one or not for adding a new pichu
# The logic to find the legal square is that from a given square is to move in all 8 directions till I reach a P or an obstacle or agent or end of the map in that direction. For any 1 direction out of 8 directions, if I hit a P before 'X'  or '@' then its not a legal square to place a new pichu
def legal_square(house_map,row,col):
    direction={"N":(-1,0),"NE":(-1,1),"E":(0,1),"SE":(1,1),"S":(1,0),"SW":(1,-1),"W":(0,-1),"NW":(-1,-1)}
    for i in direction:
        r=row
        c=col
        r=r+direction[i][0]
        c=c+direction[i][1]
        
        while  r>=0 and r<len(house_map) and c>=0 and c<len(house_map[0]):
            # if row==3 and col==6:
                # print(i,direction[i])
                # print("Functionality Check for r=3 and c=6")
                # print(r,c)
            if house_map[r][c] in ["X","@"]:
                break
            elif house_map[r][c]=="p":
                return False
            r=r+direction[i][0]
            c=c+direction[i][1]
    return True

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
    max_pichu=0
    while len(fringe) > 0:
        # print("Pradeep Reddy Rokkam")
        # print(fringe)
        # print("Length of the fringe is {}".format(len(fringe)))
        
        for new_house_map in successors( fringe.pop() ):
            pichu_current=0

            #counting the number of pichus in the current map 
            for i in new_house_map:
                for j in i:
                    if j=="p":
                        pichu_current=pichu_current+1

            # print("Count of pichus is {}".format(pichu_current)) # printing the number of pichus
            print(pichu_current, end=" ")
            # print(printable_house_map(new_house_map))
            # print("|*|"*50)
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
        
        max_pichu= max(max_pichu,pichu_current)
        # print(max_pichu,pichu_current)
        # if pichu_current<max_pichu:
        #         return ([],False)
        # print("The length of the fringe is {}".format(len(fringe)))
    return ([],False)



# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")

##########################################################################################################################
# import sys

# # Parse the map from a given filename
# def parse_map(filename):
# 	with open(filename, "r") as f:
# 		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# # Count total # of pichus on house_map
# def count_pichus(house_map):
#     return sum([ row.count('p') for row in house_map ] )

# # Return a string with the house_map rendered in a human-pichuly format
# def printable_house_map(house_map):
#     return "\n".join(["".join(row) for row in house_map])

# # Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
# def add_pichu(house_map, row, col):
#     print(row,col,"Pradeep")
#     return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]


# def legal_square(house_map,row,col):
#     direction={"N":(-1,0),"NE":(-1,1),"E":(0,1),"SE":(1,1),"S":(1,0),"SW":(1,-1),"W":(0,-1),"NW":(-1,-1)}
#     for i in direction:
#         r=row
#         c=col
#         r=r+direction[i][0]
#         c=c+direction[i][1]
#         while  r>=0 and r<len(house_map) and c>=0 and c<len(house_map) :
#             if house_map[r][c]=="X":
#                 break
#             elif house_map[r][c]=="p":
#                 return False
#             r=r+direction[i][0]
#             c=c+direction[i][1]
#     return True
        


# # Get list of successors of given house_map state
# # def successors(house_map):
# #     return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0]))  if house_map[r][c] == '.' ]

# # check if house_map is a goal state
# def is_goal(house_map, k):
#     return count_pichus(house_map) == k 

# def moves(map, row, col):
#         moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

# # Arrange agents on the map
# #
# # This function MUST take two parameters as input -- the house map and the value k --
# # and return a tuple of the form (new_house_map, success), where:
# # - new_house_map is a new version of the map with k agents,
# # - success is True if a solution was found, and False otherwise.
# #
# def solve(initial_house_map,k):
#     pichu_loc=[(row_i,col_i) for col_i in range(len(initial_house_map[0])) for row_i in range(len(initial_house_map)) if house_map[row_i][col_i]=="p"][0]
#     fringe=[(pichu_loc,0)] 
#     print(fringe) #dummy

#     visited_nodes=[pichu_loc]


#     while fringe:
#         (curr_move, curr_dist)=fringe.pop()
#         # print("Current move is {}".format(curr_move))
#         # print("For the current move {} the following are the possible moves".format(curr_move))
#         for move in moves(initial_house_map, *curr_move):
#                 # print(move)
#                 # i=i-1
#                 if legal_square(initial_house_map,move[0],move[1]):
#                         initial_house_map= add_pichu(initial_house_map,move[0],move[1])
#                         return (curr_dist+1, dirctn+d)  # return a dummy answer
#                 else:
#                         if move not in visited_nodes:
#                                 d= direction(curr_move,move)
#                                 fringe.insert(0,(move, curr_dist + 1,dirctn+d))
#                                 visited_nodes.append(move)
#         print(fringe)
#     return (-1, '')  # return a path length of -1 as there is no solution from agent me
                

#     # fringe = [initial_house_map]
    
#     # while len(fringe) > 0:
#     #     # print("Pradeep Reddy Rokkam")
#     #     # print(fringe)
#     #     for new_house_map in successors( fringe.pop() ):
#     #         print(printable_house_map(new_house_map))
#     #         print("|*|"*50)
#     #         if is_goal(new_house_map,k):
#     #             return(new_house_map,True)
#     #         fringe.append(new_house_map)



# # Main Function
# if __name__ == "__main__":
#     house_map=parse_map(sys.argv[1])
#     # This is k, the number of agents
#     k = int(sys.argv[2])
#     print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
#     solution = solve(house_map,k)
#     print ("Here's what we found:")
#     print (printable_house_map(solution[0]) if solution[1] else "False")


