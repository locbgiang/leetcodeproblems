'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Input: x = 123
Output: 321
'''
x = -2147483648
# Solution:
def reverse(x):
    string = str(x)            # conver number into string
    if string[0] == '-':      # if negative number
        string = string[1:]     # remove the sign
        string = string[::-1]     # reverse the number
        string = '-'+string      # add back in the sign
        num = int(string)       # turn back into int
        if num <= (2**31) - 1 and num >= -2**31:     # if inside of limit
            return num          # return the number
        else:
            return 0           # otherwise return 0
    else:                    # if positive number
        string = string[::-1]
        num = int(string)             # reverse and turn into string
        if num <= (2**31) - 1 and num >= -(2**31):     # return number if inside limit
            return num
        else:                   # return 0 if not in limit
            return 0
# Solution
print(reverse(x))