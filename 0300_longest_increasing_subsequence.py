"""
300. Longest Increasing Subsequence  (Medium)

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

Approach: patience sorting — keep a list where tails[i] is the smallest
tail of any increasing subsequence of length i + 1; binary-search each
number's insertion point and extend or replace.

Time:  O(n log n)
Space: O(n)
"""

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)


if __name__ == "__main__":
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert Solution().lengthOfLIS([7, 7, 7, 7]) == 1
    assert Solution().lengthOfLIS([1]) == 1
    assert Solution().lengthOfLIS([1, 2, 3]) == 3
    print("ok")
