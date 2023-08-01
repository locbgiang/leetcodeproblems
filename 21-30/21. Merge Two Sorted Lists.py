'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))


def mergeTwoLists(list1, list2):
    cur = dummy = ListNode()                # create empty listnode
    while list1 and list2:                  # run while loop while not at end
        if list1.val < list2.val:           # if list1 less than list2
            cur.next = list1                # cur.next set to list1
            cur = list1                     # cur move to list1
            list1 = list1.next              # list1 move to list1.next
        else:                               # else do list2
            cur.next = list2
            cur = list2
            list2 = list2.next
    if list1 or list2:                      # if one list run out set next to the other list
        if list1:
            cur.next = list1
        else:
            cur.next = list2
    return dummy.next


mergeTwoLists(list1,list2)