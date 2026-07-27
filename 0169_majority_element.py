"""
169. Majority Element  (Easy)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


if __name__ == "__main__":
    assert Solution().majorityElement([3, 2, 3]) == 3
    assert Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert Solution().majorityElement([1]) == 1
    assert Solution().majorityElement([5, 5, 5, 4, 4]) == 5
    print("ok")
