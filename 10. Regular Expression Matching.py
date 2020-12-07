'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
'''

s = "aaa"
p= "ab*a*c*a"

# Solution:
def isMatch(s, p):
    sCounter = 0
    pCounter = 0
    while sCounter != len(s) and pCounter != len(p):
        if s[sCounter] == p[pCounter] or p[pCounter] == '.':
            sCounter += 1
            pCounter += 1
        elif s[sCounter] !=  p[pCounter]:               
            if p[pCounter] == '*':
                if p[pCounter-1] == s[sCounter] or p[pCounter-1] == '.':
                    sCounter += 1
                    if sCounter == len(s):
                        if pCounter == len(p) - 1:
                            pCounter += 1
                        elif p[pCounter-1] == p[pCounter+1]:
                            pCounter += 1
                            while pCounter < len(p) and p[pCounter] == s[sCounter-1]:
                                pCounter += 1
                else: 
                    pCounter += 1
            else:
                pCounter += 1

    if sCounter != len(s) or pCounter != len(p):
        return False
    else:
        return True
# Solution
print(isMatch(s,p))