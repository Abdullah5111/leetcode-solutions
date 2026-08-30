"""
53. Maximum Subarray  (Medium)

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

Approach: Kadane's algorithm — extend the running sum or restart at
the current element, whichever is larger; track the best seen.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for x in nums[1:]:
            cur = max(cur + x, x)
            best = max(best, cur)
        return best


if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert Solution().maxSubArray([1]) == 1
    assert Solution().maxSubArray([5, 4, -1, 7, 8]) == 23
    assert Solution().maxSubArray([-1]) == -1
    assert Solution().maxSubArray([-2, -1]) == -1
    print("ok")
