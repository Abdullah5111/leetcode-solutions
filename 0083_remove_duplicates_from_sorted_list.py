"""
83. Remove Duplicates from Sorted List  (Easy)

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head


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
    assert _to_list(Solution().deleteDuplicates(_build([1, 1, 2]))) == [1, 2]
    assert _to_list(Solution().deleteDuplicates(_build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert _to_list(Solution().deleteDuplicates(_build([]))) == []
    assert _to_list(Solution().deleteDuplicates(_build([1, 1, 1]))) == [1]
    print("ok")
