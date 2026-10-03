"""
199. Binary Tree Right Side View  (Medium)

Given the root of a binary tree, imagine standing on its right side and
return the values of the nodes you can see, ordered top to bottom.

Approach: BFS level by level — the last node in each level is the one
visible from the right.

Time:  O(n)
Space: O(w)  (w = max level width)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        view = []
        queue = deque([root])
        while queue:
            view.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return view


if __name__ == "__main__":
    #      1
    #     / \
    #    2   3
    #     \   \
    #      5   4
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert Solution().rightSideView(root) == [1, 3, 4]
    # deepest node is on the left
    assert Solution().rightSideView(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))) == [1, 3, 4]
    assert Solution().rightSideView(TreeNode(1, None, TreeNode(3))) == [1, 3]
    assert Solution().rightSideView(None) == []
    print("ok")
