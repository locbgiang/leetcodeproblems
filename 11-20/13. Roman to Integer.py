'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Input: s = "III"
Output: 3
'''

# Solution:
def romanToInt (s):
    num = 0
    for i, char in reversed(list(enumerate(s))):
        if char == 'I':
            num += 1
        elif char == 'V':
            if i != 0 and s[i-1] == 'I':
                num += 3
            else:
                num += 5
        elif char == 'X':
            if i != 0 and s[i-1] == 'I':
                num += 8
            else:
                num += 10
        elif char == 'L':
            if i != 0 and s[i-1] == 'X':
                num += 30
            else:
                num += 50
        elif char == 'C':
            if i != 0 and s[i-1] == 'X':
                num += 80
            else:
                num += 100
        elif char == 'D':
            if i != 0 and s[i-1] == 'C':
                num += 300
            else:
                num += 500
        elif char == 'M':
            if i != 0 and s[i-1] == 'C':
                num += 800
            else:
                num += 1000
    return num

# Solution
string = 'XIV'
print(romanToInt(string))