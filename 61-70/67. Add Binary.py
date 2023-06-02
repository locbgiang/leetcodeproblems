'''
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"
'''

def addBinary(a, b):
    num_a = int(a)
    num_b = int(b)
    bin_a = bin(num_a)
    bin_b = bin(num_b)
    print(bin_a)
    print(bin_b)
    print(bin_a + bin_b)
    print(bin(12),2)
    


a = '11'
b = '1'

addBinary(a, b)