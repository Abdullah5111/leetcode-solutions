"""
1038. Binary Search Tree to Greater Sum Tree  (Medium)

Given the root of a BST, change every node's value to the original
value plus the sum of all values greater than it.

Approach: reverse in-order traversal (right, node, left) visits values
from largest to smallest, so a running sum is exactly the new value.

Time:  O(n)
Space: O(h) recursion
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running = 0

        def visit(node: Optional[TreeNode]) -> None:
            nonlocal running
            if not node:
                return
            visit(node.right)
            running += node.val
            node.val = running
            visit(node.left)

        visit(root)
        return root


def inorder(node: Optional[TreeNode]) -> List[int]:
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []


if __name__ == "__main__":
    #          4
    #       /     \
    #      1       6
    #     / \     / \
    #    0   2   5   7
    #         \       \
    #          3       8
    root = TreeNode(4,
                    TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3))),
                    TreeNode(6, TreeNode(5), TreeNode(7, None, TreeNode(8))))
    Solution().bstToGst(root)
    assert inorder(root) == [36, 36, 35, 33, 30, 26, 21, 15, 8]
    assert root.val == 30
    assert inorder(Solution().bstToGst(TreeNode(0, None, TreeNode(1)))) == [1, 1]
    print("ok")
