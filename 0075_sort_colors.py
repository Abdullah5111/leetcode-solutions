"""
75. Sort Colors  (Medium)

Given an array nums with n objects colored red, white or blue (0, 1, 2),
sort them in-place so objects of the same color are adjacent, in the
order red, white, blue — without using the library sort.

Approach: Dutch national flag, one pass with three pointers. Everything
before `lo` is 0, everything after `hi` is 2, and `mid` scans the
unknown middle: swap 0s back to `lo`, 2s forward to `hi` (without
advancing `mid`, since the swapped-in value is still unchecked).

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo = mid = 0
        hi = len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1


if __name__ == "__main__":
    for case in ([2, 0, 2, 1, 1, 0], [2, 0, 1], [0], [1, 1], [2, 2, 0, 0], [1, 2, 0, 2, 1, 0, 0]):
        nums = case[:]
        Solution().sortColors(nums)
        assert nums == sorted(case)
    print("ok")
