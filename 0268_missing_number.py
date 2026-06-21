"""
268. Missing Number  (Easy)

Given an array nums containing n distinct numbers drawn from the range [0, n],
exactly one number in that range is missing. Return it.

Approach (sum formula): the numbers 0..n add up to a known total,
n * (n + 1) / 2. Subtracting the actual sum of the array leaves exactly the one
value that was left out. Simple and intuitive, with no extra space.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)


if __name__ == "__main__":
    assert Solution().missingNumber([3, 0, 1]) == 2
    assert Solution().missingNumber([0, 1]) == 2
    assert Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution().missingNumber([0]) == 1
    assert Solution().missingNumber([1]) == 0
    print("ok")
