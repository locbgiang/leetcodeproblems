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
    current = head      # point at the head

    tempList = []       # temporary list of k length, used to reverse
    finalList = []      # this list will be turned into a linked list

    while current:      # while current pointer is not none
        tempList.append(current.val)    # append the value into templist
        if counter == k:                # check if counter is equal to k
            # if counter is equal to k we just reverse whatever in the list and add it to our final list
            tempList.reverse()          
            finalList.extend(tempList)  # using extend we add only the values and not the entire list like append
            tempList = []               # reset the temp list
            counter = 0                 # reset counter
        current = current.next          # move pointer
        counter += 1                    # count up
    # after the while loop we add whatever remains from temp list into final list 
    finalList.extend(tempList)

    # Now we just need to create a new linked list using our final list
    if finalList:            # if finallist exist
      head = ListNode(finalList[0])    # set head of list to return
      current = head                  # current pointer is head
      for value in finalList[1:]:      # a for loop starting from postion 1
          new_node = ListNode(value)  # create a new node with value from current position
          current.next = new_node     # the current pointer .next is the newly create node
          current = current.next      # move the current pointer 1 over
      return head
    else:
        return None         # finallist doesnt exist meaning we did not get input return None


reverseKGroup(first, 2)