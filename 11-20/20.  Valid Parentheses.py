
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example:
Input: s = "()"
Output: true
'''
def isValid(s):
    count = 0
    openList = []
    closeList = []
    while count < len(s):
        if s[count] == '(' or s[count] == '{' or s[count] == '[':
            openList.insert(0,s[count])
        elif s[count] == ')' or s[count] == '}' or s[count] == ']':
            closeList.insert(0, s[count])
        if len(openList) > 0:
            if s[count] == ')' and openList[0] == '(':
                openList.pop(0)
                closeList.pop(0)
            elif s[count] == '}' and openList[0] == '{':
                openList.pop(0)
                closeList.pop(0)
            elif s[count] == ']' and openList[0] == '[':
                openList.pop(0)
                closeList.pop(0)
        count += 1
    
    if len(openList) == 0 and len(closeList) == 0:
        return True
    else:
        return False

s = '{[]}'
print(isValid(s))