"""
21. Merge Two Sorted Lists  (Easy)

Given the heads of two sorted singly-linked lists, splice them together into
one sorted list and return its head. The merged list is made by reusing the
existing nodes (no new node values are created).

Approach: dummy head + tail pointer. Walk both lists, repeatedly attaching the
smaller current node to the tail and advancing that list. When one list runs
out, attach the remaining tail of the other (already sorted). Return
dummy.next.

Time:  O(m + n)
Space: O(1)   in-place relinking
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
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
    merge = Solution().mergeTwoLists
    assert _to_list(merge(_build([1, 2, 4]), _build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert _to_list(merge(_build([]), _build([]))) == []
    assert _to_list(merge(_build([]), _build([0]))) == [0]
    assert _to_list(merge(_build([5]), _build([1, 2, 3]))) == [1, 2, 3, 5]
    print("ok")
