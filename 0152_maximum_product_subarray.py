"""
152. Maximum Product Subarray  (Medium)

Given an integer array nums, find a contiguous non-empty subarray within
the array that has the largest product, and return the product.
The answer fits in a 32-bit integer.

Approach: track both the max and min running products — a negative
number swaps them, since the smallest (negative) product can become
the largest when multiplied by another negative.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            best = max(best, cur_max)
        return best


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6
    assert Solution().maxProduct([-2, 0, -1]) == 0
    assert Solution().maxProduct([-2, 3, -4]) == 24
    assert Solution().maxProduct([-2]) == -2
    assert Solution().maxProduct([0, 2]) == 2
    print("ok")
