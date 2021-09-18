# a0
Name: Pradeep Reddy Rokkam
UID: 2000766513
Assignment 0 (Elements of Artificial Intelligence)

## Problem 1:Route Pichu

###  Abstraction:

#### 1)	Set of States 
a.	All the possible states are the positions our pichu could take
i.	In this scenario, our set of states would be all different nodes where our pichu could take a position legally (‘.’,’@’,’p’)
##### 2)	Initial State S0:
a.	The node that was given in the in the initial state, where pichu is in the cell or square (5,0) 
##### 3)	A function of SUCC: S   encodes possible transitions of the system
a.	For a given cell where a pichu is at, the successor function gives all the possible squares our pichu can legally move in all compass directions (N, S, E & W) or (L, R, D, and U for left, right, down, and up) 
#### 4)	Set of Goal States:
a.	Here we have only one goal state which is ‘@’ (at square 5X6). This is the square that we want our pichu to navigate to in the shortest possible path 
#### 5)	A cost function that calculates how expensive a successor is
a.	For the given conditions, a move can only happen in one of four compass directions. And the cost is same and is 1 for moving from the given square to one of the adjacent squares. And finally, the cost function gives the cost from initial state to the goal states
i.	E.g., If a solution has a cost of 5 means that our pichu must move 5 times from the initial state to reach to the goal state  
Let’s talk about the algorithm, here we are making use of fringe data structure (using stack) to solve the problem:
	The algorithm is often giving us the wrong solution because it is getting caught in an infinite loop and this loop is occurring at the cells (2,2) and (2,3). After a certain point, our agent is only oscillating between these two squares (because our fringe is guiding the agent to do so). Since we are using a stack here, I think we are applying Depth First Search which is not a complete algorithm i.e. It does not guarantee a solution even if one exists.
	However, replacing stack to queue for implementing a fringe doesn’t solve the problem as well. Even with the fringe based on queue, it is still getting caught up in the infinite loop.  

#### Algorithm:

Algorithm that worked for me is implemented using Breadth First Search where from the initial state I check all the nodes in a systematic manner.

Reaching from Initial state to the Goal State:
*	First, I check all the nodes that are at a distance of 1
*	Then I check all the nodes that are at a distance of 2 and so on 
*	However, I achieved this mechanism using a list that has all the visited nodes. I’m aware that this will create some overhead, But I was not able apply BFS without using a list of visited nodes
*	Also, this will definitely give me a solution which is also optimal, because I am checking all the nodes in a systematic manner (this is what we expect from BFS)
Obtaining Path for the Optimal Solution:
*	I obtained the path from initial state to the goal state by making a small change to the existing fringe where I capture the path from initial node to the goal node (or any node that I visit during the navigation) that is being inserted into the fringe.
	*	Suppose I move from (5,0) to (4,0) that is move “U”, So my node (4,0) from the initial state could be reached by moving in the “U” direction
	*	And now when I move from (4,0) to (3,0), that is also again “U”. Now I add this to the existing path. So it will be “U” + ”U”. So, by moving in the direction of “UU” we will reach the node (3,0) from the initial node 
	*	By repeating this process for all the nodes, we will get the path from initial state to the goal state

## Problem 2:Arrange Pichus
### Abstraction:
#### 1)	Set of States 
a.	All the possible maps where an agent could be placed
i.	In this scenario, our set of states would be all different maps where our pichu/pichu could take a position legally i.e., no other pichu is in the same row, same column and same diagonal
#### 2)	Initial State S0:
a.	The map that was given in the in the initial state, where p is in the cell (5,0) and only one agent is in the map
#### 3)	A function of SUCC: S  encodes possible transitions of the system
a.	For a given map where the pichu/pichu’s are at, the successor function gives all the maps where an additional pichu could be placed legally 
#### 4)	Set of Goal States:
a.	Here we may or may not have more than one goal states, it could also be a case where there is no goal state i.e., We can’t arrange the given number of pichu’s without seeing them each other 
#### 5)	A cost function that calculates how expensive a successor is
a.	The cost of successor for the given state is again 1(or same) for all the successors because for all the possible maps we add new pichu to those maps. Adding a new pichu at a given location of the map (or  a 2-D list) is constant and is same  as to add a new pichu at other locations

#### Algorithm:
About the algorithm, we are using the Depth First Search Algorithm here with a couple of assumptions
*	The first pichu is fixed in its location 
*	The position of agent (‘@’) is also fixed and is considered equivalent to “X” if an agent is obscuring the view between two pichu’s

For this particular logic, I think this will give solution for whatever map we give (of course ignoring the time constraints) because we are searching the entire state space and I think logic is in such a way that it may not get caught in the loops

* The successor function will return all the maps where we can add one more pichu legally than the number of pichu’s in the given map.   
	* The logic to check whether a given square is legal to place a pichu is as follows:
		* From the given square which is “.” We move in all 8 directions that are N, E, S, W, NE, NW, SE, SW.  and for any one of these 8 directions if we meet a pichu before an obstacle” X” or “@”, or meet a pichu before we reach the end of the map (i.e. we can’t proceed any further in that direction) then that square is NOT LEGAL to insert a new pichu. In case we don’t meet any pichu in any of these 8 directions then that square is LEGAL to insert a new pichu.

#### What could be improved

The only problem with this approach could be since it is a blind search if we have bigger map, then we may have a much bigger branching factor and we may take a very long time to arrive at the solution. Probably, if we can get a heuristic function which can efficiently search the map then we can deal with the bigger maps without running the codes for a longer time.



