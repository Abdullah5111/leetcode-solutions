"""
283. Move Zeroes  (Easy)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        for n in nums:
            if n != 0:
                nums[insert] = n
                insert += 1
        for i in range(insert, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    Solution().moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]

    b = [0]
    Solution().moveZeroes(b)
    assert b == [0]

    c = [1, 2, 3]
    Solution().moveZeroes(c)
    assert c == [1, 2, 3]

    d = [0, 0, 1]
    Solution().moveZeroes(d)
    assert d == [1, 0, 0]
    print("ok")
