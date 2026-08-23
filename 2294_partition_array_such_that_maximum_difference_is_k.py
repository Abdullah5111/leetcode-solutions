"""
2294. Partition Array Such That Maximum Difference Is K  (Medium)

Time:  O(n log n)
Space: O(1)
"""

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        start = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] - start > k:
                ans += 1
                start = nums[i]
        return ans + 1


if __name__ == "__main__":
    assert Solution().partitionArray([3, 6, 1, 2, 5], 2) == 2
    assert Solution().partitionArray([1, 2, 3], 1) == 2
    assert Solution().partitionArray([2, 2, 4, 5], 0) == 3
    print("ok")
