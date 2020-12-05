'''
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

s = 'babad'
# Solution:
def longestPalindrome(s):
    def spreader(left, right):                                             # spreader function to find length of palindrome string
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    if not s: 
        return ''
    if len(s) == 1:
        return s                                            
    end = 0
    start = 0
    for i in range(len(s)):                                               # loop through s
        len1mid = spreader(i, i)                                  # find palindrome string length if it exist with 1 middle
        len2mid = spreader(i, i+1)                                # find palindrome string length if it exists with 2 middle
        max_len = max(len1mid, len2mid)                      # get the longest length between the two
        if max_len > end - start:                # if this is the longest length overall, set end and begining points
            start = i - (max_len-1) // 2
            end = i + max_len // 2
    return s[start: end+1]                     # return the string with the start and end point
# Solution
print(longestPalindrome(s))
