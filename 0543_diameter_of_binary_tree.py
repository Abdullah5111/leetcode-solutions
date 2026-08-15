"""
543. Diameter of Binary Tree  (Easy)

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def depth(node):
            nonlocal best
            if node is None:
                return 0
            lh = depth(node.left)
            rh = depth(node.right)
            best = max(best, lh + rh)
            return 1 + max(lh, rh)

        depth(root)
        return best


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
    assert Solution().diameterOfBinaryTree(_build([1, 2, 3, 4, 5])) == 3
    assert Solution().diameterOfBinaryTree(_build([1, 2])) == 1
    assert Solution().diameterOfBinaryTree(_build([1])) == 0
    print("ok")
