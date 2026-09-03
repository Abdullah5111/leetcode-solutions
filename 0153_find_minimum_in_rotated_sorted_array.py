"""
153. Find Minimum in Rotated Sorted Array  (Medium)

Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. Given such an array of unique values, find the
minimum element. The algorithm must run in O(log n) time.

Approach: binary search — compare the midpoint with the rightmost
value; a sorted (unrotated) half means the minimum lies to the left.

Time:  O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]


if __name__ == "__main__":
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert Solution().findMin([11, 13, 15, 17]) == 11
    assert Solution().findMin([2, 1]) == 1
    assert Solution().findMin([1]) == 1
    print("ok")
