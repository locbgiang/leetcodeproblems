'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)
first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

def removeNthFromEnd(head, n):
    dummy = fast = slow = ListNode(0, head)
    for i in range(n):
        fast = fast.next
        print('fast ', fast.val)
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
        print('fast ', fast.val, 'slow ', slow.val)
    slow.next = slow.next.next
    return dummy.next

head = first
n = 2
removeNthFromEnd(head,n)