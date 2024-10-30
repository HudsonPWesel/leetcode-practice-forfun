from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    previous, current = None, head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous


four = ListNode(4)
three = ListNode(3)
two = ListNode(2)
one = ListNode(1)
head = one
one.next = two
two.next = three
three.next = four

current = reverseList(head)
while current.next:
    print(current.val)
