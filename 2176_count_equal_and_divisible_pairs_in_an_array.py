"""
2176. Count Equal and Divisible Pairs in an Array  (Easy)

Time:  O(n^2)
Space: O(1)
"""

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count


if __name__ == "__main__":
    assert Solution().countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4
    assert Solution().countPairs([1, 2, 3, 4], 1) == 0
    assert Solution().countPairs([5, 5, 5, 5], 3) == 5
    print("ok")
