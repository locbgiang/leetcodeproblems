'''
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"
'''

def addBinary(a, b):
    res = ''
    carry = 0

    a, b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord(a["0"]) if i < len(a) else 0
        digitB = ord(b[i]) - ord(b["0"]) if i < len(b) else 0
        total = digitA + digitB + carry
        char = total % 2
        

a = '11'
b = '1'

addBinary(a, b)