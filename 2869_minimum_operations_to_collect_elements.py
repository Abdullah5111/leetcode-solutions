"""
2869. Minimum Operations to Collect Elements  (Easy)

Time:  O(n)
Space: O(k)
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x = k
        n = len(nums)
        i = n - 1
        flags = [0] * k
        while x:
            if nums[i] <= k and flags[nums[i]-1] == 0:
                x -= 1
                flags[nums[i]-1] = 1
            i -= 1
        return n - i - 1


if __name__ == "__main__":
    assert Solution().minOperations([3, 1, 5, 4, 2], 2) == 4
    assert Solution().minOperations([3, 1, 5, 4, 2], 5) == 5
    assert Solution().minOperations([3, 2, 5, 3, 1], 3) == 4
    assert Solution().minOperations([1], 1) == 1
    assert Solution().minOperations([2, 1, 2, 2], 2) == 3
    print("ok")
