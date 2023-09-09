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

def partition(head, x):
    while head:
        print(head.val)
        head = head.next
    return

input = [1,4,3,2,5,2]
head = llist(input)
x = 3
partition(head, x)