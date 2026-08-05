"""
206. Reverse Linked List  (Easy)

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


def _build(values):
    """Build a linked list from a Python list, return its head."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def _to_list(head):
    """Flatten a linked list back into a Python list."""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert _to_list(Solution().reverseList(_build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert _to_list(Solution().reverseList(_build([1, 2]))) == [2, 1]
    assert _to_list(Solution().reverseList(_build([]))) == []
    assert _to_list(Solution().reverseList(_build([7]))) == [7]
    print("ok")
