"""
3289. The Two Sneaky Numbers of Digitville  (Easy)

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)
        return result


if __name__ == "__main__":
    assert sorted(Solution().getSneakyNumbers([0, 1, 1, 0])) == [0, 1]
    assert sorted(Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3]
    assert sorted(Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])) == [4, 5]
    print("ok")
