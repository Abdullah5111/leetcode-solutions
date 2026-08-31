"""
238. Product of Array Except Self  (Medium)

Given an integer array nums, return an array answer such that
answer[i] is the product of all elements of nums except nums[i].
Solve it without division and in O(n).

Approach: two passes — first store the product of everything left of
each index, then sweep from the right multiplying in the running
suffix product.

Time:  O(n)
Space: O(1) extra (output array excluded)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert Solution().productExceptSelf([2, 3]) == [3, 2]
    assert Solution().productExceptSelf([1, 0]) == [0, 1]
    print("ok")
