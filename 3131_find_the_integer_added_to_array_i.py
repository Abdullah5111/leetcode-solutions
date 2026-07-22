"""
3131. Find the Integer Added to Array I  (Easy)

You are given two arrays of equal length, `nums1` and `nums2`. Each element in
nums1 has been increased (or decreased) by an integer x, so that afterwards
nums1 and nums2 become equal (same integers with the same frequencies). Return
the integer x.

Approach: adding the same x to every element shifts the whole array by x, so the
minimum of nums1 maps to the minimum of nums2. Therefore x = min(nums2) -
min(nums1). (Equivalently, the difference of any matching order statistic, e.g.
the two minimums.)

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)


if __name__ == "__main__":
    assert Solution().addedInteger([2, 6, 4], [9, 7, 5]) == 3
    assert Solution().addedInteger([10], [5]) == -5
    assert Solution().addedInteger([1, 1, 1, 1], [1, 1, 1, 1]) == 0
    print("ok")
