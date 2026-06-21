"""
169. Majority Element  (Easy)

Given an array nums of size n, return the element that appears more than n / 2
times. The majority element is guaranteed to exist.

Approach: Boyer-Moore voting. Keep a candidate and a counter. Each value either
votes for the current candidate (counter += 1) or against it (counter -= 1);
when the counter hits zero, adopt the next value as the new candidate. Because
the majority element occupies more than half the array, the votes against it can
never fully cancel it out, so it survives as the final candidate.

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
