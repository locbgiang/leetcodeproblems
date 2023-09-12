'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

def generateParenthesis(n):
    line = []
    output = []
    def backtrack(openN, closedN):
        if openN == closedN == n:               # if open == closed == n then add to output
            output.append("".join(line))
        if openN < n:                           # if open < n then create a branch
            line.append("(")
            backtrack(openN + 1, closedN)
            line.pop()
        if closedN < openN:                     # if closed < open then create a branch
            line.append(")")
            backtrack(openN, closedN + 1)
            line.pop()
    backtrack(0, 0)
    return output
        
        
n = 4
generateParenthesis(n)
