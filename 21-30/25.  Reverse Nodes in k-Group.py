'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
'''
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

first = ListNode(1)
second = ListNode(2)
third =  ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

first.next = second
second.next = third
third.next = fourth
fourth.next = fifth

def reverseKGroup(head, k):
    counter = 1
    current = head

    tempList = []
    while current:
        tempList.append(current.val)
        if counter == k:
            print(tempList)
        current = current.next
        counter += 1

    return

reverseKGroup(first, 2)