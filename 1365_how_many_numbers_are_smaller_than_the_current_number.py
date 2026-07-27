"""
1365. How Many Numbers Are Smaller Than the Current Number  (Easy)

Time:  O(n + K)  where K is the value range (101)
Space: O(K)
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 101
        for n in nums:
            counts[n] += 1

        prefix = [0] * 101
        running = 0
        for v in range(101):
            prefix[v] = running
            running += counts[v]

        return [prefix[n] for n in nums]


if __name__ == "__main__":
    assert Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
    assert Solution().smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert Solution().smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]
    assert Solution().smallerNumbersThanCurrent([5]) == [0]
    print("ok")
