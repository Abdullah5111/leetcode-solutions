"""
189. Rotate Array  (Medium)

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative. Do it in-place with O(1) extra space.

Approach: reverse the whole array, then reverse the first k and the
remaining n - k elements separately.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    nums = [-1, -100, 3, 99]
    Solution().rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
    nums = [1, 2]
    Solution().rotate(nums, 5)
    assert nums == [2, 1]
    nums = [1]
    Solution().rotate(nums, 0)
    assert nums == [1]
    print("ok")
