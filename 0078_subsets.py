"""
78. Subsets  (Medium)

Given an integer array nums of unique elements, return all possible
subsets (the power set), in any order, without duplicates.

Approach: start from [[]] and, for each number, add a copy of every
existing subset with that number appended.

Time:  O(n * 2^n)
Space: O(n * 2^n) output
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result


if __name__ == "__main__":
    out = Solution().subsets([1, 2, 3])
    assert sorted(out) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert Solution().subsets([0]) == [[], [0]]
    assert len(Solution().subsets([1, 2, 3, 4, 5])) == 32
    print("ok")
