'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Input: x = 121
Output: true
'''

x = 121

# Solution:
def isPalindrome(x):
    if x < 0:                # if x is a negative number, return false
        return False
    string = str(x)           # convert into string
    string = string[::-1]        # reverse the number
    num = int(string)       # convert back into int
    if num == x:          # if new int is equal to x, return true
        return True
    else:                # else return false
        return False
# Solution
print(isPalindrome(x))