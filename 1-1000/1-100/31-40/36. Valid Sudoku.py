'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
'''



def isValidSudoku(board):
    # check duplicate values in both x and y direction
    checkCol = [[], [], [], [], [], [], [], [], []]
    for row in range(0, 9):                         # loop through row (y direction)
        checkRow = []
        for col in range(0, 9):                     # loop through collumn (x direction)
            cur = board[row][col]       # the current value
            
            if cur not in checkRow and cur.isnumeric():     # if the current value not in checkRow and is a number
                checkRow.append(cur)                        # add it to checkRow
            elif cur in checkRow:                   # if current value is in checkRow
                return False                        # found a duplicate, return False

            if cur not in checkCol[col] and cur.isnumeric():    # same idea but for collumn
                checkCol[col].append(cur)               # add to checkCol 
            elif cur in checkCol[col]:              # if current is in checkCol
                return False                        # found duplicate in collumn, return False

    # now we check for duplicate in the 3x3 box
    for box_y in range(0, 9, 3):            # iterate by 3, (0, 3, 6)
        for box_x in range(0, 9, 3):           # iterate by 3 in the x direction (0, 3, 6)
            boxCheck = []                   #create boxCheck
            for row in range(0, 3):         #iterate through row (0, 1, 2)
                for col in range(0, 3):     # iterate through col (0,1,2)
                    cur = board[box_y + row][box_x + col]           # current position, note the box shape
                    if cur not in boxCheck and cur.isnumeric(): # same idea as above
                        boxCheck.append(cur)
                    elif cur in boxCheck:           # if cur in box, return false
                        return False
                
    return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 =[
    [".",".",".","9",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".","3",".",".",".",".",".","1"],
    [".",".",".",".",".",".",".",".","."],
    ["1",".",".",".",".",".","3",".","."],
    [".",".",".",".","2",".","6",".","."],
    [".","9",".",".",".",".",".","7","."],
    [".",".",".",".",".",".",".",".","."],
    ["8",".",".","8",".",".",".",".","."]]

board3 =[
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(board3))