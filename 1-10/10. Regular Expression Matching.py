'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
'''


s = 'a'
p = ".*..a*"


# Solution:
def isMatch(s, p):
    memo = {}
    def dp(i, j):
        if (i, j) not in memo:      # if i and j not in memory
            if j == len(p):             # if j is at the end of p
                ans = i == len(s)       # set answer = i == len of s
            else:             
                first_match = i < len(s) and p[j] in {s[i], '.'}
                print(first_match)
                if j+1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)
# Solution
print(isMatch(s,p))