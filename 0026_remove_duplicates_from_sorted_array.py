"""
26. Remove Duplicates from Sorted Array  (Easy)

Given a sorted array nums, remove duplicates in-place so each element appears
once, keeping the relative order. Return k, the number of unique elements; the
first k slots of nums must hold those unique values (the rest don't matter).

Approach: two pointers. `slow` marks the position of the last unique value
written. Scan with `fast`; whenever nums[fast] differs from the last written
value, advance slow and copy it in. k = slow + 1.

Time:  O(n)
Space: O(1)   in-place
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = Solution().removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = Solution().removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4]

    nums = []
    assert Solution().removeDuplicates(nums) == 0

    nums = [7]
    k = Solution().removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]
    print("ok")
