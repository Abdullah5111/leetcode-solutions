"""
46. Permutations  (Medium)

Given an array nums of distinct integers, return all the possible
permutations, in any order.

Approach: backtracking — swap each remaining element into the current
position, recurse on the rest, then swap back.

Time:  O(n * n!)
Space: O(n) recursion, output excluded
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def build(start: int) -> None:
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                build(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        build(0)
        return result


if __name__ == "__main__":
    from itertools import permutations
    out = Solution().permute([1, 2, 3])
    assert sorted(out) == sorted(map(list, permutations([1, 2, 3])))
    assert Solution().permute([0, 1]) in ([[0, 1], [1, 0]], [[1, 0], [0, 1]])
    assert Solution().permute([1]) == [[1]]
    assert len(Solution().permute([1, 2, 3, 4])) == 24
    print("ok")
