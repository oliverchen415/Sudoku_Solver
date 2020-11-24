#grid = [
    #[5, 3, 0, 0, 7, 0, 0, 0, 0],
    #[6, 0, 0, 1, 9, 5, 0, 0, 0],
    #[0, 9, 8, 0, 0, 0, 0, 6, 0],
    #[8, 0, 0, 0, 6, 0, 0, 0, 3],
    #[4, 0, 0, 8, 0, 3, 0, 0, 1],
    #[7, 0, 0, 0, 2, 0, 0, 0, 6],
    #[0, 6, 0, 0, 0, 0, 2, 8, 0],
    #[0, 0, 0, 4, 1, 9, 0, 0, 5],
    #[0, 0, 0, 0, 8, 0, 0, 7, 9]
#]

import numpy as np

def find_empty(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                return (row, col)
    return None

def valid(puzzle, row, col, num):
    # for rows
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # for columns
    for j in range(9):
        if puzzle[j][col] == num:
            return False

    # for boxes
    box_row = (row//3)*3
    box_col = (col//3)*3

    for i in range(3):
        for j in range(3):
            if puzzle[box_row + i][box_col + j] == num:
                return False
    return True

def solve(puzzle):
    find = find_empty(puzzle)
    if not find:
        return True
    else:
        row, col = find

    if puzzle[row][col] == 0:
        for i in range(1, 10):
            if valid(puzzle, row, col, i):
                puzzle[row][col] = i
                if solve(puzzle):
                    return True
                puzzle[row][col] = 0
    return False


#solve(grid)
#print(np.matrix(grid))
