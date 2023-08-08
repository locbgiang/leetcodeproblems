'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

def plusOne(digits):
    last_index = len(digits)-1
    while last_index > -1:
        if digits[last_index] + 1 < 10:
            digits[last_index] += 1
            return digits
        else:
            digits[last_index] = 0
            last_index -= 1
            if last_index == -1:
                digits.insert(0,1)
                return digits
    return digits


digits = [9]
plusOne(digits)
