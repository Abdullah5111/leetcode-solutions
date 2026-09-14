"""
236. Lowest Common Ancestor of a Binary Tree  (Medium)

Given a binary tree and two nodes p and q, find their lowest common
ancestor (LCA), defined as the lowest node in the tree that has both
p and q as descendants (a node may be a descendant of itself).
All node values are unique; p != q.

Approach: recurse — a node is the LCA when p and q are found in
different subtrees; otherwise bubble the found node upward.

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
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


if __name__ == "__main__":
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    root = TreeNode(3)
    five = root.left = TreeNode(5)
    one = root.right = TreeNode(1)
    six = five.left = TreeNode(6)
    two = five.right = TreeNode(2)
    zero = one.left = TreeNode(0)
    eight = one.right = TreeNode(8)
    sol = Solution()
    assert sol.lowestCommonAncestor(root, five, one) is root
    assert sol.lowestCommonAncestor(root, five, six) is five
    assert sol.lowestCommonAncestor(root, six, two) is five
    assert sol.lowestCommonAncestor(root, zero, eight) is one
    print("ok")
