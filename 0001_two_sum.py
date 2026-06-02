"""
1. Two Sum  (Easy)

Given an array of integers `nums` and an integer `target`, return indices of
the two numbers such that they add up to `target`.

Approach: single-pass hash map.
For each number x, the complement we need is `target - x`. If we've already
seen the complement, we're done. Otherwise, record x's index.

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    print("ok")
