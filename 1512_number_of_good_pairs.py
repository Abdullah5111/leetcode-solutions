"""
1512. Number of Good Pairs  (Easy)

Given an array of integers `nums`, a pair (i, j) is good if nums[i] == nums[j]
and i < j. Return the number of good pairs.

Approach: for any value that appears k times, every unordered pair of those
positions is good, contributing k*(k-1)/2 pairs. Count occurrences of each
value in one pass, then sum the combinations. Equivalently, while scanning we
add the number of equal values seen so far to the running answer.

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
