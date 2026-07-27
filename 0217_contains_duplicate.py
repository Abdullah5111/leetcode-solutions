"""
217. Contains Duplicate  (Easy)

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
