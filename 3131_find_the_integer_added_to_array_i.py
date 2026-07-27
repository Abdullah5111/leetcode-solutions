"""
3131. Find the Integer Added to Array I  (Easy)

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
