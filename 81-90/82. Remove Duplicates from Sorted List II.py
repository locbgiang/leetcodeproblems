'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:
Input: head = [1,1,1,2,3]
Output: [2,3]
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
sixth = ListNode(4)
seventh = ListNode(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth
sixth.next = seventh

def deleteDuplicates(head):
    answer = ListNode(0, head)
    prev = answer
    cur = head

    while cur:
        if cur.next and cur.val == cur.next.val:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur.next
        else:
            prev = prev.next
        cur = cur.next
    return answer.next

deleteDuplicates(first)