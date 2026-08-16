"""
572. Subtree of Another Tree  (Easy)

Time:  O(n * m)  n, m = node counts of root and subRoot
Space: O(h)  h = tree height (recursion stack)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if a is None or b is None:
                return a is b
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        if root is None:
            return subRoot is None
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


def _build(values):
    """Build a tree from a level-order list (None for missing), return root."""
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    assert Solution().isSubtree(_build([3, 4, 5, 1, 2]), _build([4, 1, 2])) is True
    assert Solution().isSubtree(_build([3, 4, 5, 1, 2, None, None, None, None, 0]), _build([4, 1, 2])) is False
    assert Solution().isSubtree(_build([1, 1]), _build([1])) is True
    print("ok")
