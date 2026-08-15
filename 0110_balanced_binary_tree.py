"""
110. Balanced Binary Tree  (Easy)

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            if lh == -1:
                return -1
            rh = height(node.right)
            if rh == -1 or abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return height(root) != -1


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
    assert Solution().isBalanced(_build([3, 9, 20, None, None, 15, 7])) is True
    assert Solution().isBalanced(_build([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert Solution().isBalanced(_build([])) is True
    print("ok")
