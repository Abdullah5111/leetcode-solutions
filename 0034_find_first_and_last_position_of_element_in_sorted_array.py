"""
34. Find First and Last Position of Element in Sorted Array  (Medium)

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value. If target is not
found, return [-1, -1]. Must run in O(log n).

Approach: two lower-bound binary searches — the first index >= target
gives the start, and the first index >= target + 1, minus one, gives the
end. If the start is out of range or not equal to target, it's absent.

Time:  O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x: int) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        start = lower_bound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, lower_bound(target + 1) - 1]


if __name__ == "__main__":
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert Solution().searchRange([], 0) == [-1, -1]
    assert Solution().searchRange([1], 1) == [0, 0]
    assert Solution().searchRange([2, 2, 2, 2], 2) == [0, 3]
    assert Solution().searchRange([1, 2, 3], 4) == [-1, -1]  # past the end
    print("ok")
