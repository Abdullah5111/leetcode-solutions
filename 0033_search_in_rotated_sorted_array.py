"""
33. Search in Rotated Sorted Array  (Medium)

An ascending array of distinct integers is possibly rotated at an
unknown pivot. Given the array and a target, return its index or -1.
The algorithm must run in O(log n) time.

Approach: binary search — at every step one half is sorted; check
whether the target lies in that half's range and discard accordingly.

Time:  O(log n)
Space: O(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


if __name__ == "__main__":
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert Solution().search([1], 0) == -1
    assert Solution().search([3, 1], 1) == 1
    assert Solution().search([5, 1, 3], 5) == 0
    assert Solution().search([1, 2, 3, 4, 5], 4) == 3
    print("ok")
