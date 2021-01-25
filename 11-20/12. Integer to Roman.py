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
However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Input: num = 3
Output: "III"
'''

# Solution:
def intToRoman(num):
    roman = ''
    while num > 0:
        if num <= 3:
            num -= 1
            roman = roman + 'I'
        elif num <=4:
            num -= 4
            roman = roman + 'IV'
        elif num <= 8:
            num -= 5
            roman = roman + 'V'
        elif num <= 9:
            roman = roman + 'IX'
            num -= 9
        elif num <= 39:
            num -= 10
            roman = roman + 'X'
        elif num <= 49:
            roman = roman + 'XL'
            num -= 40
        elif num <= 89:
            num -= 50
            roman = roman + 'L'
        elif num <= 99:
            roman = roman + 'XC'
            num -= 90
        elif num <= 399:
            num -= 100
            roman = roman + 'C'
        elif num <= 499:
            roman = roman + 'CD'
            num -= 400
        elif num <= 899:
            num -= 500
            roman = roman + 'D'
        elif num <= 999:
            roman = roman + 'CM'
            num -= 900
        else:
            num -= 1000
            roman = roman + 'M'
    return roman
# Solution
inputNum = 1994
print(intToRoman(inputNum))