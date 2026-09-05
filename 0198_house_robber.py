"""
198. House Robber  (Medium)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed; adjacent houses have
connected security systems, so you cannot rob two adjacent houses.
Given nums, return the maximum amount you can rob tonight.

Approach: DP with two rolling values — at each house take the larger
of robbing it (plus the best two back) or skipping it.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for x in nums:
            prev, curr = curr, max(prev + x, curr)
        return curr


if __name__ == "__main__":
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([2, 1, 1, 2]) == 4
    assert Solution().rob([5]) == 5
    assert Solution().rob([]) == 0
    print("ok")
