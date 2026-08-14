"""
112. Path Sum  (Easy)

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum == root.val
        rest = targetSum - root.val
        return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)


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
    assert Solution().hasPathSum(_build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) is True
    assert Solution().hasPathSum(_build([1, 2, 3]), 5) is False
    assert Solution().hasPathSum(_build([]), 0) is False
    assert Solution().hasPathSum(_build([1, 2]), 1) is False
    print("ok")
