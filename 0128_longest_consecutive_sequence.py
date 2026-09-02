"""
128. Longest Consecutive Sequence  (Medium)

Given an unsorted array of integers nums, return the length of the
longest consecutive elements sequence. An algorithm that runs in O(n)
time is required.

Approach: put all numbers in a set; only start counting from numbers
whose predecessor is absent (sequence starts), then walk forward.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            length = 1
            while num + length in nums_set:
                length += 1
            best = max(best, length)
        return best


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert Solution().longestConsecutive([]) == 0
    assert Solution().longestConsecutive([1, 2, 0, 1]) == 3
    print("ok")
