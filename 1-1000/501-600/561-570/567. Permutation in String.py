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
    len_s1, len_s2 = len(s1), len(s2)

    if len_s1 > len_s2:
        return False

    char_count_s1 = [0] * 26
    char_count_s2 = [0] * 26

    # Initialize char_count_s1 and char_count_s2 for the first window
    for i in range(len_s1):
        char_count_s1[ord(s1[i]) - ord('a')] += 1
        char_count_s2[ord(s2[i]) - ord('a')] += 1

    for i in range(len_s2 - len_s1):
        # Check if the current window is a permutation of s1
        if char_count_s1 == char_count_s2:
            return True

        # Move the window by updating char_count_s2
        char_count_s2[ord(s2[i]) - ord('a')] -= 1
        char_count_s2[ord(s2[i + len_s1]) - ord('a')] += 1

    # Check the last window
    return char_count_s1 == char_count_s2
    
s1 = 'ab'
s2 = 'eidbaooo'
checkInclusion(s1, s2)