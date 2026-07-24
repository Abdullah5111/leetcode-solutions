"""
2605. Form Smallest Number From Two Digit Arrays  (Easy)

Given two arrays of unique digits `nums1` and `nums2`, return the smallest
number that contains at least one digit from each array.

Approach: two cases.
  * If the arrays share a digit, a single-digit number suffices — the smallest
    common digit is the answer.
  * Otherwise the smallest number needs one digit from each array, i.e. two
    digits. Take the smallest digit of each array and place the smaller one in
    the tens place: min(a, b) * 10 + max(a, b).

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
