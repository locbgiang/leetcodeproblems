'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''

def lengthOfLastWord(s):
    pointer = len(s)-1
    length = 0
    while s[pointer] == ' ':
        pointer -= 1
    while pointer >= 0 and s[pointer] != ' ':
        length += 1
        pointer -= 1
    return length

s = 'Hello World'

print(lengthOfLastWord(s))