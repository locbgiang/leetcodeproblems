'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
'''
from os import curdir


class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

def llist(input):
    cur = ListNode()
    answer = cur
    for i in input:
        cur.next = ListNode(i)
        cur = cur.next
    return answer.next
'''
def partition(head, x):
    cur = head
    prev = left = answer = ListNode(0, cur)
    right = False
    
    while cur:
        if cur.val >= x:
            right = True
        
        if cur.val < x and not right:
            left = cur
            prev = cur
            cur = cur.next
        elif cur.val < x and right:
            temp = left.next
            left.next = cur
            left = left.next
            prev.next = cur.next
            cur.next = temp
            cur = prev.next
        else:
            prev = cur
            cur = cur.next
    return answer.next
'''
def partition(head, x):
    slist, blist = ListNode(), ListNode()
    small, big = slist, blist
    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            big.next = head
            big = big.next
        head = head.next
    small.next = big
    big.next = None
    return slist.next
input = [1,4,3,0,5,2]
head = llist(input)
x = 2
partition(head, x)