"""
3190. Find Minimum Operations to Make All Elements Divisible by Three  (Easy)

Each operation adds or subtracts 1 from any element. Return the minimum number
of operations to make every element divisible by 3.

Approach: for any integer, the nearest multiple of 3 is at most 1 away
(remainder 1 -> step down, remainder 2 -> step up), so each non-divisible
element costs exactly one operation. The answer is just how many elements
aren't already divisible by 3.

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for x in nums if x % 3 != 0)


if __name__ == "__main__":
    assert Solution().minimumOperations([1, 2, 3, 4]) == 3  # 1,2,4 each need one
    assert Solution().minimumOperations([3, 6, 9]) == 0     # all divisible
    assert Solution().minimumOperations([10]) == 1
    print("ok")
