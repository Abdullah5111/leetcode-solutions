"""
235. Lowest Common Ancestor of a Binary Search Tree  (Medium)

Given a binary search tree (BST) and two nodes p and q, find their
lowest common ancestor — the lowest node with both p and q as
descendants (a node may be a descendant of itself).

Approach: walk from the root using the BST order — if both targets are
smaller go left, if both larger go right, else the node is the LCA.

Time:  O(h)
Space: O(1)
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
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return node


if __name__ == "__main__":
    #        6
    #      /   \
    #     2     8
    #    / \   / \
    #   0   4 7   9
    #      / \
    #     3   5
    root = TreeNode(6)
    two = root.left = TreeNode(2)
    eight = root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    four = two.right = TreeNode(4)
    four.left = TreeNode(3)
    four.right = TreeNode(5)
    seven = eight.left = TreeNode(7)
    eight.right = TreeNode(9)
    sol = Solution()
    assert sol.lowestCommonAncestor(root, two, eight) is root
    assert sol.lowestCommonAncestor(root, two, four) is two
    assert sol.lowestCommonAncestor(root, four.left, four.right) is four
    assert sol.lowestCommonAncestor(root, seven, eight) is eight
    print("ok")
