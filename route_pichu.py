#!/usr/local/bin/python3
#
# route_pichu.py : a maze solver
#
# Submitted by : Pradeep Reddy Rokkam, prokkam@iu.edu, UID :2000766513
#
# Based on skeleton code provided in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")
        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Find the direction of the move from the two given moves(current move and future move)
def direction(current_move,future_move):
        if current_move[0]<future_move[0]:
                return "D"
        elif current_move[0]>future_move[0]:
                return "U"
        elif current_move[1]<future_move[1]:
                return "R"
        else:
                return "L"

# Perform search on the map
#
# This function MUST take a single parameter as input -- the house map --
# and return a tuple of the form (move_count, move_string), where:
# - move_count is the number of moves required to navigate from start to finish, or -1
#    if no such route exists
# - move_string is a string indicating the path, consisting of U, L, R, and D characters
#    (for up, left, right, and down)

def search(house_map):
        # Find pichu start position
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0,"")] # Made a small change to the fringe, where we add a path from to reach to that node from initial node
        print(fringe) #dummy

        visited_nodes=[pichu_loc]

        # i=100 # A dummy varible i, where we break out of the loop after 100 iterations

        while fringe:
                # if i<0:
                #         break 
                # print(i)
                # print("\n")
                (curr_move, curr_dist, dirctn)=fringe.pop() 
                # print("Current move is {}".format(curr_move))
                # print("For the current move {} the following are the possible moves".format(curr_move))
                for move in moves(house_map, *curr_move):
                        # print(move)
                        # i=i-1
                        if house_map[move[0]][move[1]]=="@":
                                print("Goal Reached {}".format(curr_dist+1))
                                d= direction(curr_move,move)
                                return (curr_dist+1, dirctn+d)  # return the answer distance and the path
                        else:
                                if move not in visited_nodes:
                                        d= direction(curr_move,move)
                                        fringe.insert(0,(move, curr_dist + 1,dirctn+d))
                                        visited_nodes.append(move)
                print(fringe)
        return (-1, '')  # return a path length of -1 as there is no solution from agent me
                

        

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        # print(house_map)
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + solution[1])
        print("Test Check")


