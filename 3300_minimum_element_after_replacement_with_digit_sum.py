"""
3300. Minimum Element After Replacement With Digit Sum  (Easy)

Time:  O(n * d)  (d = digits per number)
Space: O(1)
"""

from typing import List


class Solution:
    def calc_sum(self, n):
        s = 0
        while n:
            s += n%10
            n = n // 10
        return s

    def minElement(self, nums: List[int]) -> int:
        m = self.calc_sum(nums[0])
        for n in nums:
            x = self.calc_sum(n)
            if x < m:
                m = x
        return m


if __name__ == "__main__":
    assert Solution().minElement([10, 12, 13, 14]) == 1
    assert Solution().minElement([1, 2, 3, 4]) == 1
    assert Solution().minElement([999, 19, 199]) == 10
    print("ok")
