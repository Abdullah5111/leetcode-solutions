"""
3925. Concatenation with Reversal  (Easy)

Return the array formed by appending the reverse of nums to nums itself —
i.e. result = nums + reversed(nums), length 2n.

Approach: walk i over 0..n-1 and append nums[n-i-1], which visits the elements
back-to-front. The loop bound n is captured up front, so the elements appended
during iteration are never re-read.

Time:  O(n)
Space: O(1) extra (the output reuses/extends the input list)
"""
from typing import List


class Solution:
    def concatWithReverse(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[n - i - 1])
        return nums


if __name__ == "__main__":
    assert Solution().concatWithReverse([1, 2, 3]) == [1, 2, 3, 3, 2, 1]
    assert Solution().concatWithReverse([5]) == [5, 5]
    assert Solution().concatWithReverse([1, 2]) == [1, 2, 2, 1]
    print("ok")
