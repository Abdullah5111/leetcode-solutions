"""
141. Linked List Cycle  (Easy)

Time:  O(n)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def _build_with_cycle(values, pos):
    """Build a list from `values`; if pos >= 0, link the tail back to node at index pos."""
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if nodes and pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    assert Solution().hasCycle(_build_with_cycle([3, 2, 0, -4], 1)) is True
    assert Solution().hasCycle(_build_with_cycle([1, 2], 0)) is True
    assert Solution().hasCycle(_build_with_cycle([1, 2], -1)) is False
    assert Solution().hasCycle(_build_with_cycle([], -1)) is False
    print("ok")
