"""
1480. Running Sum of 1d Array  (Easy)

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
