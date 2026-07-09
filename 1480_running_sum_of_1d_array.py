"""
1480. Running Sum of 1d Array  (Easy)

Given an array `nums`, the running sum is defined as
runningSum[i] = sum(nums[0..i]). Return the running sum of `nums`.

Approach: keep a rolling total. Walk the array once, add each element to the
running total, and store the total in place. Updating in place keeps space O(1)
beyond the output the caller already owns.

Time:  O(n)
Space: O(1)  (in-place)
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i, x in enumerate(nums):
            total += x
            nums[i] = total
        return nums


if __name__ == "__main__":
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert Solution().runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert Solution().runningSum([5]) == [5]
    print("ok")
