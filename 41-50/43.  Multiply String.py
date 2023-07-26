'''
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''

def multiply(num1, num2):
    if num1=='0' or num2=='0':
        return '0'
    
    mem = {'0':0, '1': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}

    int_num1 = 0
    for i, num in enumerate(reversed(num1)):        # convert string to int, we reverse the str
        pow = 1 
        while i > 0:                            # instead of 10**i, we can use this while loop to determind the position
            pow *= 10
            i -= 1
        int_num1 += mem[num] * pow             # (i=0 pow=1) (i=1 pow=10) (i=2 pow=100) ect. add to int_num1

    # same idea as above
    int_num2 = 0
    for i, num in enumerate(reversed(num2)):
        pow = 1
        while i > 0:
            pow *= 10
            i -= 1
        int_num2 += mem[num] * pow

    # do a mulitply
    int_answer = int_num1 * int_num2
    answer = ''
    while int_answer > 0:               # save as string
        answer += str(int_answer%10)
        int_answer //= 10
    return answer[::-1]


num1 = "123"
num2 = "456"
multiply(num1, num2)