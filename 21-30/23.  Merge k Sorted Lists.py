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
  tempList = []         # create a temporary array
  for i in lists:       # break down the list of list
    while i:            # going through each list
      tempList.append(i.val)  # adding value of linked list
      i = i.next              # go next link list 
  tempList.sort()       # sort
  
  # now we just need to create a merged linked-list
  if tempList:            # if templist exist
      head = ListNode(tempList[0])    # set head of list to return
      current = head                  # current pointer is head
      for value in tempList[1:]:      # a for loop starting from postion 1
          new_node = ListNode(value)  # create a new node with value from current position
          current.next = new_node     # the current pointer .next is the newly create node
          current = current.next      # move the current pointer 1 over
      return head
  else:
      return None         # templist dont exist meaning we did not get input return None
    


mergeKLists(lists)
