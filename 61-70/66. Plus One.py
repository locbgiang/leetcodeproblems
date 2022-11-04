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

'''
def plusOne(digits):
    digit = int("".join(map(str,digits)))
    digit += 1
    output = []
    for d in str(digit):
        output.append(d)
    return output
'''    

def plusOne(digits):
    digits = digits[::-1]                   # reverse list
    one, i = 1, 0                           # one is to keep track of remainder, i is pointer
    while one:                          # while there is remainder
        if i < len(digits):                # counter is less than length of list
            if digits[i] == 9:             # digit at counter is 9
                digits[i] = 0               # set it to 0
            else:                       # else add 1 to number at counter and remove remainder
                digits[i] += 1
                one = 0
        else:                       # add 1 to list at the end of list (case: 99 = 100)
            digits.append(1)
            one = 0
        i += 1                  # move counter up
    return digits[::-1]



digits = [1,2,3]
plusOne(digits)
