from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    current = head
    list_len = 0

    while current:
        list_len += 1
        current = current.next

    if list_len <= 1:
        return None

    # current = 1

    distance = math.ceil(list_len / n)  # 1
    prev, selected_el = None, head

    for i in range(distance):
        if i + 1 == distance:
            prev = selected_el
        selected_el = selected_el.next

    prev.next = selected_el.next
    selected_el.next = None

    return head


el = ListNode(5)
head = el
print(removeNthFromEnd(head, 1))
