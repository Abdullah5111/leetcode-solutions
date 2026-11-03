"""
896. Monotonic Array  (Easy)

An array is monotonic if it is either monotone increasing or monotone
decreasing. Given an integer array nums, return true if it is monotonic.

Approach: a monotonic array already equals its own sorted copy, either
ascending or descending — sort two copies and compare.

Time:  O(n log n)
Space: O(n)
"""


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        a = nums.copy()
        b = nums.copy()
        a.sort()
        b.sort()
        b.reverse()
        return nums == a or nums == b


if __name__ == "__main__":
    assert Solution().isMonotonic([1, 2, 2, 3]) is True
    assert Solution().isMonotonic([6, 5, 4, 4]) is True
    assert Solution().isMonotonic([1, 3, 2]) is False
    assert Solution().isMonotonic([5]) is True
    assert Solution().isMonotonic([2, 2, 2]) is True
    print("ok")
