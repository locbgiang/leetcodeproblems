'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
first = ListNode(1)
second = ListNode(4)
third =  ListNode(5)
first.next = second
second.next = third

fourth = ListNode(1)
fifth = ListNode(3)
sixth = ListNode(4)
fourth.next = fifth
fifth.next = sixth

seventh = ListNode(2)
eighth = ListNode(6)
seventh.next = eighth

lists = [first, fourth, seventh]

def mergeKLists (lists):
  for i in lists:
    print(i.val)

mergeKLists(lists)