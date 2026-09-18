"""
102. Binary Tree Level Order Traversal  (Medium)

Given the root of a binary tree, return the level order traversal of
its nodes' values (left to right, level by level).

Approach: BFS with a queue — process one level at a time by draining
whatever is in the queue, collecting children for the next level.

Time:  O(n)
Space: O(n)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().levelOrder(root) == [[3], [9, 20], [15, 7]]
    assert Solution().levelOrder(None) == []
    assert Solution().levelOrder(TreeNode(1)) == [[1]]
    print("ok")
