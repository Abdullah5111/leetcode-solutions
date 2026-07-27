"""
1822. Sign of the Product of an Array  (Easy)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                negatives += 1
        return -1 if negatives % 2 else 1


if __name__ == "__main__":
    assert Solution().arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
    assert Solution().arraySign([1, 5, 0, 2, -3]) == 0
    assert Solution().arraySign([-1, 1, -1, 1, -1]) == -1
    assert Solution().arraySign([1, 2, 3]) == 1
    print("ok")
