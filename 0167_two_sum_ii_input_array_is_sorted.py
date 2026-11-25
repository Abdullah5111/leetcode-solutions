"""
167. Two Sum II - Input Array Is Sorted  (Medium)

Given a 1-indexed array of integers numbers sorted in non-decreasing
order, find two numbers that add up to target and return their indices
[index1, index2] (1-indexed, index1 < index2). Exactly one solution
exists, and only constant extra space may be used.

Approach: two pointers from both ends — if the sum is too small, move
the left pointer right; if too big, move the right pointer left. The
sorted order guarantees no valid pair is skipped.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            total = numbers[lo] + numbers[hi]
            if total == target:
                return [lo + 1, hi + 1]
            if total < target:
                lo += 1
            else:
                hi -= 1
        return []


if __name__ == "__main__":
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
    assert Solution().twoSum([1, 2, 3, 4, 4, 9], 8) == [4, 5]  # duplicate values
    print("ok")
