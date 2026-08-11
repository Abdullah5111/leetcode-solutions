"""
448. Find All Numbers Disappeared in an Array  (Easy)

Time:  O(n)
Space: O(1)  (ignoring the output; marks in place)
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, x in enumerate(nums) if x > 0]


if __name__ == "__main__":
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution().findDisappearedNumbers([1, 1]) == [2]
    assert Solution().findDisappearedNumbers([1]) == []
    print("ok")
