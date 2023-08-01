'''
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]
'''
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

first = ListNode(1)
second = ListNode(2)
third =  ListNode(3)
fourth = ListNode(4)

first.next = second
second.next = third
third.next = fourth

def swapPairs(head):
    #check if there are 2 nodes
    if not head or not head.next:
        print('no nodes')
        return head
    
    # create a prev node
    dummy = ListNode(0)
    dummy.next = head

    # point current node to head
    currNode = head
    prev = dummy

    # switch current with next
    while currNode and currNode.next:
        # switch 
        currNext = currNode.next        # currNext is current node next
        currNode.next = currNext.next   # currNode.next move to one after currNext.next
        currNext.next = currNode        # move currNext.next to point at current node  
        prev.next = currNext

        # move pointer forward
        prev = currNode                 
        currNode = currNode.next

    return dummy.next


swapPairs(first)