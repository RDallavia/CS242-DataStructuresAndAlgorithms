#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
7/16/2016
CS242 - LAB 7

The following program instantiates a maze as a grid object, prints the unsolved
maze, solves the maze using a BFS/backtracking routine and queue, prints the solved maze,
and returns the coordinates of visited cells to a file entitled solution.txt.
Accompanying Grid Class provided by Lambert, Kenneth A. (2014) modified by 
student to accept maze on instnatiation. Since no instruction as to "how"
to implement a queue was provided, "deque" was used, as it comes with 
both .append() and .popleft(). 

1). The term "choice point" wants for clarification.  At every step of through
the maze, possible moves are examined and choices are assessed. Every move, therefore, 
is a potential "choice point." Based on this definition, the route pursued via a 
stack implementation hit 210 "choice points," whereas the queue implementation hit
266 "choice points."   If a "choice point" is a point in the maze where the player
has two or more viable paths from which to chose, then the stack implementation
faces approximately 8 such points (the near circular areas present a counting problem).
The queue implementation cmpletes the entire maze before locating the exit, and finds
two more "choice points" under this definition (i.e., 10).

2.) The stack implementation solving the maze is a DFS process, while the process below (using a queue) is 
BFS. Perofrmance-wise, they are generally equivalent. That said, a printout of the queue
suggests it gets more "backed up" than a stack. I know DFS and BFS not from the book, but
from working with graphs. If you'd like to search something exhaustively, DFS is generally
what one chooses. For something like the shortest distance between person A and person B on
Twitter, BFS is the better option. A printout of the queue reveals that the algoritm below is, indeed,
checking everything. The maze confirms as much. Leaving no stone unturned, it's not exactly shocking
this implementation goes thru more steps.  

3). A best case maze for both stacks and queues isn't much of a maze: It's a linear corridor of
unit length that can be traversed from beginning to end with no choice but to advance forward to the end
being made by the algorithm along the way. A straight (left-to-right) corridor of unit length 
would require one trip through the loop containing the algorithm's main logic. A more complex 
best-case maze for stacks (DFS) would likely entail one that minimizes decision points and is fairly 
compact, as all squares will be checked. A best-case, queue-based (BFS) solution would be similarly 
compact in size, but would place the end of the maze as few removes away from the beginning as possible. 
Worst-case mazes for stacks (DFS) would have no solution and/or would be of the largest size possible, 
maximizing the number of suqares to explore. A worst-case maze for queue-based (BFS) solutions would 
either have no solution, a solution set extremely far from the starting point, or the solution sequested in what 
would otherwise be called a connected component, separated from the main graph (if the maze were 
conceptualized as such), and thus unreachable. Extensive size would add to the difficultly. 

"""
from grid import Grid
from collections import deque

def getMaze(text_file):
    '''Reads in maxe data from extenal file'''
    rows = 0
    maze = []
    input_file = open("maze1.maz", "r")
    for line in input_file:
        rows += 1
        cols = 0
        # note for author: watch where you instantiate lists -- this was a huge problem
        fill_values = []
        for character in line:
            fill_values.append(character)
            # a hacky method of fixing the col count, which is 57
            if cols < 57:
                cols += 1
        maze.append(fill_values)
    input_file.close()
    return (rows, cols, maze)

def main():
    maze_data = getMaze("maze1.maz")
    rows = maze_data[0]
    cols = maze_data[1]
    maze = maze_data[2]
    # convert maze data to grid object
    maze_grid = Grid(rows, cols, maze)
    print("Unsolved Maze")
    print("--------------")
    print(maze_grid)
    queue = deque()
    # repository for routes examined
    route = []
    # locate starting point
    for i in range(rows):
        for j in range(cols):
            # "P" designates the starting point in the maze file 
            if maze_grid[i][j] == "P":
                queue.append((i,j))
                break
            
    while len(queue):
        #print(queue)
        location = queue.popleft()
        # stop if maze exit found, as denoted by the letter "T"
        if maze_grid[location[0]][location[1]] == "T":
            print("Solved Maze")
            print("-----------")
            print(maze_grid)
            # write coordinates of cells visited to output file
            output_file = open("solution.txt", "w")
            cells = list()
            for coordinates in route:
                cells.append(coordinates)
            output_file.write(str(cells))
            output_file.write(str(len(route)))
            output_file.close()
            return True
        # explore cells adjacent to start if vacant; add them to stack and route lists
        elif not maze_grid[location[0]][location[1]] is ".":
            maze_grid[location[0]][location[1]] = "."
            # advance along same row, one col over
            if location[1]+1 < cols and maze_grid[location[0]][location[1]+1] in [" ", "T"]:
                queue.append((location[0],location[1]+1))
                route.append((location[0],location[1]+1))
            # one row down, same col
            if location[0]+1 < rows and maze_grid[location[0]+1][location[1]] in [" ", "T"]:
                queue.append((location[0]+1,location[1]))
                route.append((location[0]+1,location[1]))
            # one row up, same col
            if location[0]-1 >= rows-rows and maze_grid[location[0]-1][location[1]] in [" ", "T"]:
                queue.append((location[0]-1,location[1]))
                route.append((location[0]-1,location[1]))
            # same row, one col back
            if location[1]-1 >= cols-cols and maze_grid[location[0]][location[1]-1] in [" ", "T"]:
                queue.append((location[0],location[1]-1))
                route.append((location[0],location[1]-1))
    
    return False
            
if __name__ == '__main__':
    main()

            
        