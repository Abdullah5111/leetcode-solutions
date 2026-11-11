"""
19. Remove Nth Node From End of List  (Medium)

Given the head of a linked list, remove the nth node from the end of the
list and return its head.

Approach: two pointers with a gap of n — move `fast` n steps ahead, then
advance both until `fast` hits the last node; `slow` now sits just before
the node to delete. A dummy head handles removing the first node.

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


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
    assert _to_list(Solution().removeNthFromEnd(_build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert _to_list(Solution().removeNthFromEnd(_build([1]), 1)) == []
    assert _to_list(Solution().removeNthFromEnd(_build([1, 2]), 1)) == [1]
    assert _to_list(Solution().removeNthFromEnd(_build([1, 2]), 2)) == [2]  # remove head
    print("ok")
