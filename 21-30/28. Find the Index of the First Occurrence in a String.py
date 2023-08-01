'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "sadbutsad", needle = "sad"
    Output: 0
    Explanation: "sad" occurs at index 0 and 6.
    The first occurrence is at index 0, so we return 0.

Example 2:
    Input: haystack = "leetcode", needle = "leeto"
    Output: -1
    Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''

def strStr(haystack, needle):
    # get endpoint for forloop since there is no point looping pass the end point as there are not enough letters left in haystack to make needle
    end = len(haystack) - len(needle) + 1
    # we will for loop through haystack one letter at a time 
    for position in range(0, end):
        # if we found a letter in haystack matching the first letter of needle
        if haystack[position] == needle[0]:
            temp = ''           # create a temp string
            for i in range(0, len(needle)):     # loop through length of needle
                temp += haystack[i+position]    # capture the portion of haystack
            if temp == needle:              # if that portion is exactly the same as needle
                return position             # return the current position of haystack

    return -1         # no needle found in haystack return -1

haystack = 'sadbutsad'
needle = 'sad'
print(strStr(haystack, needle))