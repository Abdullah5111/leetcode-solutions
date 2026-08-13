"""
101. Symmetric Tree  (Easy)

Time:  O(n)
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a, b):
            if a is None or b is None:
                return a is b
            return a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left)

        return root is None or mirror(root.left, root.right)


def _build(values):
    """Build a tree from a BFS/level-order list (None for missing), return root."""
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
    assert Solution().isSymmetric(_build([1, 2, 2, 3, 4, 4, 3])) is True
    assert Solution().isSymmetric(_build([1, 2, 2, None, 3, None, 3])) is False
    assert Solution().isSymmetric(_build([1])) is True
    assert Solution().isSymmetric(_build([])) is True
    print("ok")
