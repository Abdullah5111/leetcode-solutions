"""
217. Contains Duplicate  (Easy)

Given an integer array nums, return True if any value appears at least twice,
and False if every element is distinct.

Approach: walk the array once, keeping a set of values already seen. If the
current value is already in the set we found a duplicate; otherwise add it.
A set gives O(1) average membership checks, so one pass is enough.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


if __name__ == "__main__":
    assert Solution().containsDuplicate([1, 2, 3, 1]) is True
    assert Solution().containsDuplicate([1, 2, 3, 4]) is False
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert Solution().containsDuplicate([]) is False
    assert Solution().containsDuplicate([7]) is False
    print("ok")
