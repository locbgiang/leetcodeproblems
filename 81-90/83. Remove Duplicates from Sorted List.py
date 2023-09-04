'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
first = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(3)
fifth = ListNode(4)
sixth = ListNode(5)
seventh = ListNode(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh

def deleteDuplicates(head):
    prev = head
    answer = prev
    while prev:
        cur = prev.next
        if cur and prev.val == cur.val:
            while cur and prev.val == cur.val:
                cur = cur.next
            prev.next = cur
        else:
            prev = prev.next
    
    while answer:
        print(answer.val)
        answer = answer.next
    return

head = [1, 1, 2]
deleteDuplicates(first)