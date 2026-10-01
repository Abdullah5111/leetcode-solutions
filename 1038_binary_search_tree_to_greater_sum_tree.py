"""
1038. Binary Search Tree to Greater Sum Tree  (Medium)

Given the root of a BST, change every node's value to the original
value plus the sum of all values greater than it.

Approach: collect all values, sort them, and build a map from each
value to the sum of every value >= it (running sum from the largest).
Then walk the tree and swap each value for its mapped sum.

Time:  O(n log n)
Space: O(n)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def collect_values(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return [node.val] + self.collect_values(node.left) + self.collect_values(node.right)

    def replace_values(self, node: Optional[TreeNode], greater_sum: dict) -> None:
        if not node:
            return
        node.val = greater_sum[node.val]
        self.replace_values(node.left, greater_sum)
        self.replace_values(node.right, greater_sum)

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = sorted(self.collect_values(root))

        greater_sum = {}
        running = 0
        for value in reversed(values):
            running += value
            greater_sum[value] = running

        self.replace_values(root, greater_sum)
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
