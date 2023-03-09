from pprint import pprint

#finds the next row and column where there is no answer, the blank box is represented as -1. 
#Returns the row and column if found. Returns none if all of the spaces are completed.
def find_next_empty(puzzle):
    
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

#determines if the guess is valid. Returns T or F.
#the number cannot be repeated in the row, column, or 3x3 box.
def is_valid(puzzle, guess, row, col):

    #every list represents a row, goes to the row index and if the guess is in the row, returns false.
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 

#creating a new list for only the column values in a row, if the guess is in the column list, returns false.
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

#dividing the rows and columns by 3, and leaving out the remainder. This is so it can be seen whether the row/column is in the 1st set of 3x3, second set 3x3, etc.
    row_start = (row // 3) * 3  #multiplying by 3 to get the index
    col_start = (col // 3) * 3


#iteration over the 3 rows and columns. if the guess is in the 3x3, returns false.
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

#returns true if guess is a solution
    return True


#solving using backtracking
def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

#if there are no empty spots, it is done.
    if row is None:  
        return True

#checks if guess is a solution  
    for guess in range(1, 10): 
        if is_valid(puzzle, guess, row, col):
            
            #if guess is a solution, the solution is placed in the puzzle
            puzzle[row][col] = guess

            #recursively call function 
            if solve_sudoku(puzzle):
                return True
        
        #resetting the value if the guess is not a valid answer. 
        puzzle[row][col] = -1

#no numbers work. puzzle is not solvable.
    return False

#example of sudoku board being solved.
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)