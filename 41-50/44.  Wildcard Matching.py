'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
'''
'''
def isMatch(s, p):
    if p == '' and s == '':
        return True  

    if len(p) > 1:
        if p[0] == '*' and p[0] == p[1]:
            return isMatch(s, p[1:])
    if s and p:
        if p[0] == '*':
            if len(p) > 1:
                if s[0] == p[1] or p[1] == '?' or p[1] == '*':
                    if isMatch(s, p[1:]):
                        return True
                if len(s) > 1:
                    if s[1] == p[1] or p[1] == '?' or p[1] == '*':
                        if isMatch(s[1:], p[1:]):
                            return True
            return isMatch(s[1:], p[0:])
        elif s[0] == p[0] or p[0] == '?':
            return isMatch(s[1:],p[1:])
    elif not s and p:
        if p[0] == '*':
            return isMatch(s, p[1:])
    return False
'''
'''
sPointer = 0
    pPointer = 0
    while pPointer < len(p) and sPointer < len(s):
        if p[pPointer] == '*':
            if starPath(s[sPointer+1:], p[pPointer+1:]):
                sPointer += 1
                pPointer += 1
            elif starPath(s[sPointer:], p[pPointer+1:]):
                pPointer += 1
            else:
                sPointer += 1
        elif s[sPointer] == p[pPointer] or p[pPointer] == '?':
            sPointer += 1
            pPointer += 1

    if not s and not p:
        return True
    elif not s and p:
        return starPath(s, p)
    else:
        return False

'''

def isMatch(s, p):
    # Backtracking
    # this function checks the validity of each path that we could take with *
    def starPath(s, p):     
        if not s and not p:
            return True                 # if there is no s or p we return True
        elif s and p:
            if p[0] == '*':             # IMPORTANT: if the head of p is a new star we return True
                return True
            elif s[0] == p[0] or p[0] == '?':       # if s[0] and p[0] are the same, move forward
                return starPath(s[1:],p[1:])
        elif not s and p:               # if there is no s but p we call this function again
            if p[0] == '*': 
                return starPath(s, p[1:])       # since a * can represent nothing we can move ignore first letter of p
        else:
            return False                # this means there is an s with no p OR there is p that isnt *, return False 
    
    if not s and not p:
        return True
    elif s and p:
        if p[0] == '*':
            if starPath(s, p[1:]):              # call starPath function by ignoring * and move p forward by 1
                return isMatch(s, p[1:])        # if the path is valid move p forward
            elif starPath(s[1:], p[1:]):                # call starpath function moving both s and p forward
                return isMatch(s[1:], p[1:])            # if the path is valid move both forward
            else:
                return isMatch(s[1:], p)        # if none of the path is valid, we move forward with s, keeping p on *
        elif s[0] == p[0] or p[0] == '?':
            return isMatch(s[1:], p[1:])
    elif not s and p:
        return starPath(s, p)
    else:
        return False

        

#bbbbbbbabbaabbabbbbaaabbabbabaaabbababbbabbbabaaabaab
s = "abcde"
p = "*?*?*?*?*?"
print(isMatch(s, p))