'''
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"
'''

def addBinary(a, b):
    answer = ''
    carry = 0
    a, b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        if i < len(a):
            digitA = int(a[i])
        else:
            digitA = 0

        if i < len(b):
            digitB = int(b[i])
        else:
            digitB = 0
        
        total = digitA + digitB + carry
        carry = total // 2
        total = total % 2
        answer = str(total) + answer
    if carry > 0:
        answer = str(carry) + answer
    return answer

a = '1111'
b = '1111'

addBinary(a, b)