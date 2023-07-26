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



def isMatch(s, p):
    # since a * can represent nothing, one letter, or multiple letters
    # we use this function to check the validity of each path that we could take with *
    def starPath(s, p):
        if not s and not p:
            return True                 
        elif s and p:
            if p[0] == '*':
                # IMPORTANT: if the head of p is a new star we return True
                return True
            elif s[0] == p[0] or p[0] == '?':
                # if s[0] and p[0] are the same, move both s and p forward
                # call starPath again until we can determind if this path is valid
                return starPath(s[1:],p[1:])
        elif not s and p:
            # since * can be nothing, we can ignore it          
            if p[0] == '*': 
                return starPath(s, p[1:])       
            else:
                return False
        else:
            # this means there is s with no p OR there is p that isnt just *, return False 
            return False                
    
    #----------- START HERE --------------
    if not s and not p:
        return True
    elif s and p:
        if p[0] == '*':         
            if starPath(s, p[1:]):
                # call starPath function by ignoring * and move p forward by 1
                # if the path is valid move p forward
                return isMatch(s, p[1:])        
            elif starPath(s[1:], p[1:]):
                # call starpath function check validity of moving both s and p forward
                # if valid move both forward
                return isMatch(s[1:], p[1:])
            else:
                # if none of the path is valid, we move forward with s, keeping p on *
                return isMatch(s[1:], p)        
        elif s[0] == p[0] or p[0] == '?':
            # if s[0] and p[0] are the same, move both forward 
            return isMatch(s[1:], p[1:])
    elif not s and p:
        # call starPath to handle no s but p
        return starPath(s, p)
    else:
        return False


s = "aa"
p = "a"
print(isMatch(s, p))
        

