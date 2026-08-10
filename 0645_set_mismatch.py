"""
645. Set Mismatch  (Easy)

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * (n + 1)
        for x in nums:
            counts[x] += 1
        duplicate = missing = 0
        for v in range(1, n + 1):
            if counts[v] == 2:
                duplicate = v
            elif counts[v] == 0:
                missing = v
        return [duplicate, missing]


if __name__ == "__main__":
    assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]
    assert Solution().findErrorNums([1, 1]) == [1, 2]
    assert Solution().findErrorNums([2, 2]) == [2, 1]
    assert Solution().findErrorNums([3, 2, 2]) == [2, 1]
    print("ok")
