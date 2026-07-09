"""
1929. Concatenation of Array  (Easy)

Given an integer array `nums` of length n, build an array `ans` of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n. In other
words, `ans` is `nums` concatenated with itself.

Approach: Python list concatenation does exactly this. `nums + nums` produces a
new list containing the elements of `nums` twice, in order.

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
