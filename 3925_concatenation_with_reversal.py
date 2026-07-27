"""
3925. Concatenation with Reversal  (Easy)

Time:  O(n)
Space: O(1) extra in-place / O(n) for the slice (a fresh output list)
"""

from typing import List


class Solution:
    def concatWithReverse(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[n - i - 1])
        return nums

    def concatWithReverseSlice(self, nums: List[int]) -> List[int]:
        return nums + nums[::-1]


if __name__ == "__main__":
    for method in ("concatWithReverse", "concatWithReverseSlice"):
        fn = getattr(Solution(), method)
        assert fn([1, 2, 3]) == [1, 2, 3, 3, 2, 1]
        assert fn([5]) == [5, 5]
        assert fn([1, 2]) == [1, 2, 2, 1]
    print("ok")
