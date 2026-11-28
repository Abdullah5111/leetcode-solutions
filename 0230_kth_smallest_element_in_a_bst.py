"""
230. Kth Smallest Element in a BST  (Medium)

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.

Approach: an inorder traversal of a BST visits values in sorted order.
Walk it iteratively with a stack and stop at the kth node popped, so
only the left spine plus k nodes are touched.

Time:  O(h + k)
Space: O(h)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


def bst_from(values):
    """Build a BST by inserting values in order."""
    root = None
    for v in values:
        if root is None:
            root = TreeNode(v)
            continue
        cur = root
        while True:
            if v < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(v)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = TreeNode(v)
                    break
                cur = cur.right
    return root


if __name__ == "__main__":
    assert Solution().kthSmallest(bst_from([3, 1, 4, 2]), 1) == 1
    assert Solution().kthSmallest(bst_from([5, 3, 6, 2, 4, 1]), 3) == 3
    assert Solution().kthSmallest(bst_from([1]), 1) == 1
    tree = bst_from([8, 4, 12, 2, 6, 10, 14])
    assert [Solution().kthSmallest(tree, k) for k in range(1, 8)] == [2, 4, 6, 8, 10, 12, 14]
    print("ok")
