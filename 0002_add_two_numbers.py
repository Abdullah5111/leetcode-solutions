"""
2. Add Two Numbers  (Medium)

Two non-empty linked lists represent two non-negative integers, one digit per
node, stored in reverse order (ones digit first). Add them and return the sum
as a linked list in the same reverse-order form.

Approach: walk both lists together like grade-school addition. At each step sum
the two current digits plus the carry, push (sum % 10) as a new node, and keep
(sum // 10) as the next carry. Continue while either list has nodes left or a
carry remains — so a final carry (e.g. 5 + 5 -> 0 -> 1) adds a leading node.

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
    # 342 + 465 = 807
    assert _to_list(add(_build([2, 4, 3]), _build([5, 6, 4]))) == [7, 0, 8]
    # 0 + 0 = 0
    assert _to_list(add(_build([0]), _build([0]))) == [0]
    # 9999999 + 9999 = 10009998 (carry propagates, longer than both inputs)
    assert _to_list(
        add(_build([9, 9, 9, 9, 9, 9, 9]), _build([9, 9, 9, 9]))
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("ok")
