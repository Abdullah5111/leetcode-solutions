"""
55. Jump Game  (Medium)

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your
maximum jump length at that position. Return true if you can reach the
last index, or false otherwise.

Approach: greedy — track the farthest reachable index; if the current
index ever passes it, the end is unreachable.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + jump)
        return True


if __name__ == "__main__":
    assert Solution().canJump([2, 3, 1, 1, 4]) is True
    assert Solution().canJump([3, 2, 1, 0, 4]) is False
    assert Solution().canJump([0]) is True
    assert Solution().canJump([0, 1]) is False
    assert Solution().canJump([2, 0, 0]) is True
    print("ok")
