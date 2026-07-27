"""
3190. Find Minimum Operations to Make All Elements Divisible by Three  (Easy)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x % 3 != 0)


if __name__ == "__main__":
    assert Solution().minimumOperations([1, 2, 3, 4]) == 3
    assert Solution().minimumOperations([3, 6, 9]) == 0
    assert Solution().minimumOperations([10]) == 1
    print("ok")
