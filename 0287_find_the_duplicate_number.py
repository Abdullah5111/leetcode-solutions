"""
287. Find the Duplicate Number  (Medium)

Given an array of n + 1 integers where each integer is in [1, n],
there is exactly one repeated number. Find it without modifying the
array and using O(1) extra space.

Approach: Floyd's cycle detection — array indices point to values, so
the duplicate is the cycle entrance; slow/fast pointers meet, then a
fresh pointer from the start meets slow at the entrance.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    assert Solution().findDuplicate([1, 3, 4, 2, 2]) == 2
    assert Solution().findDuplicate([3, 1, 3, 4, 2]) == 3
    assert Solution().findDuplicate([1, 1]) == 1
    assert Solution().findDuplicate([2, 2, 2, 2, 2]) == 2
    print("ok")
