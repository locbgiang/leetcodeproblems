'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false
'''


# ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 

def isNumber(s):
    digit, dec, e, symbol = False, False, False, False
    for c in s:
        if c in '0123456789':
            digit = True
        elif c in '+-':
            if symbol or digit or dec:
                return False
            else:
                symbol = True
        elif c in 'Ee':
            if not digit or e:
                return False
            else:
                e = True
                symbol = False
                digit = False
                dec = False
        elif c == '.':
            if dec or e:
                return False
            else:
                dec = True
        else:
            return False
    return digit


s = "0"
isNumber(s)