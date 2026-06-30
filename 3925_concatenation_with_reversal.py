"""
3925. Concatenation with Reversal  (Easy)

Return the array formed by appending the reverse of nums to nums itself —
i.e. result = nums + reversed(nums), length 2n.

Approach 1 (in-place): walk i over 0..n-1 and append nums[n-i-1], which visits
the elements back-to-front. The loop bound n is captured up front, so the
elements appended during iteration are never re-read.

Approach 2 (slice): nums + nums[::-1] builds the same result without mutating
the input — terser and arguably clearer, at the cost of an extra list.

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
        # Non-destructive: leaves the caller's list untouched.
        return nums + nums[::-1]


if __name__ == "__main__":
    for method in ("concatWithReverse", "concatWithReverseSlice"):
        fn = getattr(Solution(), method)
        assert fn([1, 2, 3]) == [1, 2, 3, 3, 2, 1]
        assert fn([5]) == [5, 5]
        assert fn([1, 2]) == [1, 2, 2, 1]
    print("ok")
