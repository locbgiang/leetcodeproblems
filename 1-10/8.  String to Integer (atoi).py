'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, 
and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. If the numerical value is out of the range of representable values, 231 − 1 or −231 is returned.

Input: str = "42"
Output: 42
'''

s = '42'
# Solution:
def myAtoi(s):
    max_int = (2**31) - 1
    min_int = -(2**31)
    negative = False
    string = ''
    numCounter = 0
    signCounter = 0
    array = s.split()

    if len(s) == 0 or len(array)==0:                  # return 0 if string is nothing
        return 0

    for i in array[0]:                              # loop through the first non white space string
        if i.isdigit():                         # if i is a number
            string += i                        # add it to final string
            numCounter += 1
        elif i == '-' and numCounter == 0 and signCounter == 0:   # if there is no number in string, and this is the first - sign
            signCounter += 1                                    # increase sign counter
            negative = True                                   # anounce that this is a negative number we're working with
        elif i == '+' and numCounter == 0 and signCounter == 0:   # if there is no number in string, and this is the first + sign
            signCounter += 1                                  # increase sign counter
            next
        else:                                  # else break out of for loop
            break
    if string:
        num = int(string)                       # turn everything from string into an interger
        if negative == True:
            num = -num
        if num > max_int:                        # if the number is over limit, return the limit
            return max_int
        elif num < min_int:
            return min_int
        else:                                 # otherwise return the number
            return num
    else:
        return 0

# Solution

print(myAtoi(s))
