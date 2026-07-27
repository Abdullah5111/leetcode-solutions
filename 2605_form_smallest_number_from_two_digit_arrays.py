"""
2605. Form Smallest Number From Two Digit Arrays  (Easy)

Time:  O(n + m)
Space: O(n + m)
"""

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)
        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)


if __name__ == "__main__":
    assert Solution().minNumber([4, 1, 3], [5, 7]) == 15
    assert Solution().minNumber([3, 5, 2, 6], [3, 1, 7]) == 3
    assert Solution().minNumber([1], [9]) == 19
    assert Solution().minNumber([5], [5]) == 5
    print("ok")
