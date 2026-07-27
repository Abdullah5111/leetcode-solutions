"""
2. Add Two Numbers  (Medium)

Time:  O(max(m, n))
Space: O(max(m, n))   for the output list
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
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
    add = Solution().addTwoNumbers
    assert _to_list(add(_build([2, 4, 3]), _build([5, 6, 4]))) == [7, 0, 8]
    assert _to_list(add(_build([0]), _build([0]))) == [0]
    assert _to_list(
        add(_build([9, 9, 9, 9, 9, 9, 9]), _build([9, 9, 9, 9]))
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("ok")
