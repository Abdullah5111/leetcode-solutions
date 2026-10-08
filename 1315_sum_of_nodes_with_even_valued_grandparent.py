"""
1315. Sum of Nodes with Even-Valued Grandparent  (Medium)

Time:  O(n)
Space: O(h) recursion
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, nd):
        x = 0
        if nd.val % 2 == 0:
            if nd.left:
                if nd.left.left:
                    x += nd.left.left.val
                if nd.left.right:
                    x += nd.left.right.val
            if nd.right:
                if nd.right.left:
                    x += nd.right.left.val
                if nd.right.right:
                    x += nd.right.right.val
        if nd.left:
            x += self.helper(nd.left)
        if nd.right:
            x += self.helper(nd.right)
        return x

    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        ans = self.helper(root)
        return ans


if __name__ == "__main__":
    #            6
    #          /   \
    #         7     8
    #        / \   / \
    #       2   7 1   3
    #      /   / \     \
    #     9   1   4     5
    root = TreeNode(6,
                    TreeNode(7, TreeNode(2, TreeNode(9)), TreeNode(7, TreeNode(1), TreeNode(4))),
                    TreeNode(8, TreeNode(1), TreeNode(3, None, TreeNode(5))))
    assert Solution().sumEvenGrandparent(root) == 18
    assert Solution().sumEvenGrandparent(TreeNode(1)) == 0
    assert Solution().sumEvenGrandparent(TreeNode(2, TreeNode(1, TreeNode(5)))) == 5
    print("ok")
