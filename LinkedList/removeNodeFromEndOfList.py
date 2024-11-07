from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    '''
  You are given the beginning of a linked list head, and an integer n.


  Remove the nth node from the end of the list

  return the beginning of the list.

  Input: head = [1,2,3,4], n = 2
  Output: [1,2,4]



  Input: head = [5], n = 1
  Output: []

  Starting from the end of the list remove n-hops from end

  - Select elemnt to remove
  - Remove that elemment

  - prev
  '''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    dummy = ListNode(0, head)
    l = dummy
    r = head

    for _ in range(n):
        r = r.next

    prev = None

    while r:
        l = l.next
        r = r.next

    l.next = l.next.next

    return dummy.next
