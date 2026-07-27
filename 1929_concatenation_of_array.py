"""
1929. Concatenation of Array  (Easy)

Time:  O(n)
Space: O(n)  (for the returned array)
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    assert Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert Solution().getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert Solution().getConcatenation([5]) == [5, 5]
    print("ok")
