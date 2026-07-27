"""
268. Missing Number  (Easy)

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
