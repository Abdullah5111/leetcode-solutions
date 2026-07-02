"""
35. Search Insert Position  (Easy)

Given a sorted array of distinct integers and a target, return the index of the
target if found, otherwise the index where it would be inserted to keep the
array sorted. Must run in O(log n).

Approach: binary search for the leftmost position whose value is >= target. The
half-open range [lo, hi) shrinks until lo == hi, which is exactly that insertion
point (and equals the target's index when present).

Time:  O(log n)
Space: O(1)
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2  # found
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1  # insert middle
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4  # insert end
    assert Solution().searchInsert([1, 3, 5, 6], 0) == 0  # insert front
    assert Solution().searchInsert([], 5) == 0
    print("ok")
