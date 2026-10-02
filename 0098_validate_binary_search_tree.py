"""
98. Validate Binary Search Tree  (Medium)

Given the root of a binary tree, determine if it is a valid BST: every
node's left subtree holds only smaller values, its right subtree only
larger values, and both subtrees are BSTs themselves.

Approach: recurse with an open (low, high) bound — each node must sit
strictly inside the range inherited from all its ancestors.

Time:  O(n)
Space: O(h) recursion
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not low < node.val < high:
                return False
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    assert Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))) is True
    # 5 -> right 4 is smaller than root
    assert Solution().isValidBST(
        TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))) is False
    # 6 sits in 3's left subtree... but 6 > root 5 — only the bound catches it
    assert Solution().isValidBST(
        TreeNode(5, TreeNode(3, None, TreeNode(6)), TreeNode(7))) is False
    assert Solution().isValidBST(TreeNode(2, TreeNode(2))) is False
    assert Solution().isValidBST(None) is True
    print("ok")
