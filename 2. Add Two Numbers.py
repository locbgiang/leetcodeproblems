'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def get_val(self):
        return self.val
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next

# l1 = [2,4,3]
l1 = ListNode(2)
l1.set_next(ListNode(4))
l1.get_next().set_next(ListNode(3))

# l2 = [5,6,4]
l2 = ListNode(5)
l2.set_next(ListNode(6))
l2.get_next().set_next(ListNode(4))

# Solution:
def addTwoNumbers(l1, l2):
        firstNum = []
        secondNum = []
        while l1 is not None:
            firstNum.append(str(l1.val))
            l1 = l1.next
        
        while l2 is not None:
            secondNum.append(str(l2.val))
            l2 = l2.next
        
        firstNum.reverse()                            # reverse the numbers
        secondNum.reverse()
        
        firstNum = int("".join(firstNum))             # combine the list into one number
        secondNum = int("".join(secondNum))
        
        
        finalNum = firstNum + secondNum               # do the addition of the two numbers
        finalNum = str(finalNum)                    # change answer to string
        finalNum = list(finalNum)             # split each number into array
        finalNum.reverse()                    # reverse the array
        
        finalList = ListNode(finalNum[0])       # initialize the linked list
        lastNode = finalList
        
        for i in range(1, len(finalNum)):                 # create the linked list
            lastNode.next = ListNode(finalNum[i])
            lastNode = lastNode.next
        return finalList
# Solution
print(addTwoNumbers(l1,l2))