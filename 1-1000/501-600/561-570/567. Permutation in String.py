'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
def checkInclusion(s1, s2):
    s1Len, s2Len = len(s1), len(s2)

    if s1Len > s2Len:
        return False

    # creates two 26 sized arrays, filled with 0s
    s1Count = [0] * 26
    s2Count = [0] * 26

    # count the letters in size s1Len window, 'a' goes in 0, 'b' goes in 1 ect.
    for i in range(s1Len):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    
    #  move the window on s2,
    for i in range(s2Len - s1Len):
        
        # if the two sCount arrays are equal, return True
        if s1Count == s2Count:
            return True

        # delete left letter, add in next letter
        s2Count[ord(s2[i]) - ord('a')] -= 1
        s2Count[ord(s2[i+s1Len]) - ord('a')] += 1
    
    return s1Count == s2Count

    
s1 = 'adc'
s2 = 'dcda'
print(checkInclusion(s1, s2))