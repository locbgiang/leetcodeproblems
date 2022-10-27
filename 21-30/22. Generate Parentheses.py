'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
'''

def generateParenthesis(n):
    output = []
    open = '('
    close = ')'
    stri = ''
    for i in range (0, n):
        stri = stri + open
        stri = stri + close
    print(stri)
n = 2
generateParenthesis(n)

# open open open close close close
# open open close open close close
# open open close close open close
# open close open open close close
# open close open close open close