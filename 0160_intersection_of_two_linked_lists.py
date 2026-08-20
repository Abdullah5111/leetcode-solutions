"""
160. Intersection of Two Linked Lists  (Easy)

Time:  O(n + m)
Space: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a


def _build_intersection(list_a, list_b, shared):
    """Build lists A and B whose tails both continue into `shared` (a Python list).
    Returns (headA, headB, intersection_node_or_None)."""
    def link(values):
        dummy = ListNode()
        tail = dummy
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next, tail

    shared_head, _ = link(shared) if shared else (None, None)
    headA, tailA = link(list_a)
    headB, tailB = link(list_b)
    if tailA:
        tailA.next = shared_head
    else:
        headA = shared_head
    if tailB:
        tailB.next = shared_head
    else:
        headB = shared_head
    return headA, headB, shared_head


if __name__ == "__main__":
    headA, headB, inter = _build_intersection([4, 1], [5, 6, 1], [8, 4, 5])
    assert Solution().getIntersectionNode(headA, headB) is inter

    headA, headB, inter = _build_intersection([1, 9, 1], [3], [2, 4])
    assert Solution().getIntersectionNode(headA, headB) is inter

    headA, headB, _ = _build_intersection([2, 6, 4], [1, 5], [])
    assert Solution().getIntersectionNode(headA, headB) is None
    print("ok")
