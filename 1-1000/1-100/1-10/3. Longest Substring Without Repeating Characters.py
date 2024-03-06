'''
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

# Solution:
def lengthOfLongestSubstring(s):
    answer = 0
    left = 0
    charSet = set()
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        answer = max(answer, right - left + 1)
    return answer
        
    
# Solution

s = 'abcabcbb'
lengthOfLongestSubstring(s)