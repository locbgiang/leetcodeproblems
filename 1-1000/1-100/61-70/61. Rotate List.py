'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


num1 = ListNode(1)
num2 = ListNode(2)
num3 = ListNode(3)
num4 = ListNode(4)
num5 = ListNode(5)
num1.next = num2
num2.next = num3
num3.next = num4
num4.next = num5


def rotateRight(head, k):
    if not head or not k:       # if head is empty or k = 0, return head
        return head

    last, length = head, 1      # last pointer, length of linked list
    while last.next:
        last = last.next        # if last.next is None we have found last
        length += 1             # count to find length of linked list

    last.next = head            # last pointer to head
    for i in range(length - k % length):        # (length - k % length) will find the new last pointer
        last = last.next                        
    newHead = last.next         # set newhead as last.next
    last.next = None            # set new last.next to point to None

    return newHead
        

k = 2
print(rotateRight(num1, k))