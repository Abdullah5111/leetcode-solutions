"""
105. Construct Binary Tree from Preorder and Inorder Traversal  (Medium)

Given two integer arrays preorder and inorder (unique values) of the
same binary tree, construct and return the tree.

Approach: the next preorder value is the current subtree's root; its
position in inorder splits the left and right subtrees. A value->index
map makes that lookup O(1), and a shared preorder pointer avoids slicing.

Time:  O(n)
Space: O(n)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {val: i for i, val in enumerate(inorder)}
        next_root = 0

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            nonlocal next_root
            if lo > hi:
                return None
            val = preorder[next_root]
            next_root += 1
            mid = index_of[val]
            return TreeNode(val, build(lo, mid - 1), build(mid + 1, hi))

        return build(0, len(inorder) - 1)


def preorder_of(node: Optional[TreeNode]) -> List[int]:
    return [node.val] + preorder_of(node.left) + preorder_of(node.right) if node else []


def inorder_of(node: Optional[TreeNode]) -> List[int]:
    return inorder_of(node.left) + [node.val] + inorder_of(node.right) if node else []


if __name__ == "__main__":
    cases = [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        ([-1], [-1]),
        ([1, 2, 3], [3, 2, 1]),  # left-only chain
        ([1, 2, 3], [1, 2, 3]),  # right-only chain
    ]
    for pre, ino in cases:
        root = Solution().buildTree(pre, ino)
        assert preorder_of(root) == pre and inorder_of(root) == ino
    root = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert (root.val, root.left.val, root.right.val) == (3, 9, 20)
    print("ok")
