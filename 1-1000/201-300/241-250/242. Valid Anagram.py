'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''
def isAnagram(s, t):
    sCounter, tCounter = {}, {}
    for i in range(0, len(s)):
        sCounter[s[i]] = sCounter.setdefault(s[i], 0) + 1
        tCounter[t[i]] = tCounter.setdefault(t[i], 0) + 1
    return sCounter == tCounter
    

s = "anagram" 
t = "nagaram"

print(isAnagram(s, t))

'''
Three different solution:

sCount, tCount = Counter(s), Counter(t)
return sCount == tCount
-----------------------------------------------------------
if len(s) != len(t):
    return False
for i in s:
    if i in t:
        t = t.replace(i, '', 1)
    else:
        return False
return True
-----------------------------------------------------------
return sorted(s) == sorted(t)
'''