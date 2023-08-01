'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
 
'''

def longestValidParentheses(s):
    arr = [-1]
    answer = 0

    for i, x in enumerate(s):
        if x == '(':
            arr.append(i)           # save position of every open
        else:
            arr.pop()               # pop last open for every close
            if not arr:
                arr.append(i)
            else:
                answer = max(answer, i - arr[-1])       # compare between current answer and position - last closed
    return answer


test = '((((())'

print(longestValidParentheses(test))