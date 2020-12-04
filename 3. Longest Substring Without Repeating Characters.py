'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

s = 'abcabcbb'

# Solution:
def lengthOfLongestSubstring(s):
    answerString = ''
    maxLength = 0
    for letter in s:
        if letter in answerString:                     # if letter is already in string, delete the string from start
            while letter in answerString:              # until that letter is deleted
                answerString = answerString[1:]
            answerString += str(letter)                # add that letter to the end of the string
        else:
            answerString+=str(letter)                  # just add letter if it's not in answerstring
        if maxLength < len(answerString):    
            maxLength = len(answerString)              # keep track of the highest max length
    return maxLength
# Solution

print(lengthOfLongestSubstring(s))