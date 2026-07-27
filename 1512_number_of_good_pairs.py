"""
1512. Number of Good Pairs  (Easy)

Time:  O(n)
Space: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(c * (c - 1) // 2 for c in counts.values())


if __name__ == "__main__":
    assert Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert Solution().numIdenticalPairs([1, 1, 1, 1]) == 6
    assert Solution().numIdenticalPairs([1, 2, 3]) == 0
    assert Solution().numIdenticalPairs([7]) == 0
    print("ok")
