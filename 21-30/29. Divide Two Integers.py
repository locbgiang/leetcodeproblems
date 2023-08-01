'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-2^31, 2^31 - 1]. 
For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
'''

def divide(dividend, divisor):
    if dividend == -(1 << 31) and divisor == -1:
        return (1 << 31) - 1
        
    negative = (dividend < 0) ^ (divisor < 0)           # find out if answer will be negative
    dividend = abs(dividend)
    divisor = abs(divisor)

    answer = 0
    current_divisor = divisor
    count = 1               # count is to keep track of how many times current divisor is multiplied by

    # run loop while the DIVIDEND is greater/equal DIVISOR
    while dividend >= divisor:
        while dividend >= current_divisor:
            print('dividend divisor answer current_divisor count')
            print(dividend,'        ', divisor,'    ', answer,'    ', current_divisor,'             ', count)
            # 
            dividend -= current_divisor         # dividend - current_divisor
            answer += count                     # add up the count

            # this is a trick for large number, instead of multiplying we are using << for bit manipulation
            current_divisor <<= 1               # equivalent of multiplying by 2, moving to the next bit
            count <<= 1                         # equivalent of multiplying by 2

        current_divisor >>= 1               # we move back to the previous bit until current divisor is smaller than what left of dividend
        count >>= 1
    return -answer if negative else answer
    '''
    # does not work with large dividend and small divisor, time out error
    while dividend >= divisor:
        dividend -= divisor
        answer += 1
    return -answer if negative else answer
    '''

dividend = 100
divisor = 2
print(divide(dividend, divisor))