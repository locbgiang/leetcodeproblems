'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''

s = 'AB'
numRows = 1

def convert(s, numRows):
    memory = {}
    down = True
    row = 0
    if numRows == 1:                   # if there is one row, return the string
        return s
    for letter in s:
        if down is True:
            if row not in memory:          # store in dictionary for the first time
                memory[row] = letter
            else:
                memory[row] += letter       # add to dictionary 
            row += 1                # go to next row
            if row == numRows:     # if this row is the max (outside of bound 0,1,2 for 3 rows)
                down = False       # no longer go down
                row -= 1           # go back
        else:                # going up
            row -= 1         # go up one from last row
            memory[row] += letter       # add the letter to row
            if row == 0:           # if row at 0
                down = True        # start going down
                row += 1         # go down one since 0 is already used.
    finalString = ''
    for key in memory:
        finalString += memory[key]        # combine all strings from memory into a single string
    return finalString
convert(s, numRows)