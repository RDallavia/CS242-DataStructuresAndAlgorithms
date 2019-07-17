#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ryan C. Dallavia
7/8/2016
CS242 - LAB 6

The following program instantiates a maze as a grid object, prints the unsolved
maze, solves the maze using a DFS/backtracking routine, prints the solved maze,
and returns the coordinates of visited cells to a file entitled solution.txt.
Accompanying Grid Class provided by Lambert, Kenneth A. (2014) modified by 
student to accept maze on instnatiation. 
"""
from grid import Grid

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
    stack1 = []
    # repository for routes examined
    route = []
    # locate starting point
    for i in range(rows):
        for j in range(cols):
            # "P" designates the starting point in the maze file 
            if maze_grid[i][j] == "P":
                stack1.append((i,j))
                break
            
    while len(stack1):
        location = stack1.pop()
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
            output_file.close()
            return True
        # explore cells adjacent to start if vacant; add them to stack and route lists
        elif not maze_grid[location[0]][location[1]] is ".":
            maze_grid[location[0]][location[1]] = "."
            # advance along same row, one col over
            if location[1]+1 < cols and maze_grid[location[0]][location[1]+1] in [" ", "T"]:
                stack1.append((location[0],location[1]+1))
                route.append((location[0],location[1]+1))
            # one row down, same col
            if location[0]+1 < rows and maze_grid[location[0]+1][location[1]] in [" ", "T"]:
                stack1.append((location[0]+1,location[1]))
                route.append((location[0]+1,location[1]))
            # one row up, same col
            if location[0]-1 >= rows-rows and maze_grid[location[0]-1][location[1]] in [" ", "T"]:
                stack1.append((location[0]-1,location[1]))
                route.append((location[0]-1,location[1]))
            # same row, one col back
            if location[1]-1 >= cols-cols and maze_grid[location[0]][location[1]-1] in [" ", "T"]:
                stack1.append((location[0],location[1]-1))
                route.append((location[0],location[1]-1))
    return False
            
if __name__ == '__main__':
    main()

            
        