"""
136. Single Number  (Easy)

Time:  O(n)
Space: O(1)
"""

from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


if __name__ == "__main__":
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber([1]) == 1
    assert Solution().singleNumber([7, 3, 7]) == 3
    print("ok")
