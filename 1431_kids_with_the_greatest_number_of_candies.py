"""
1431. Kids With the Greatest Number of Candies  (Easy)

Given `candies` where candies[i] is the number of candies the i-th kid has, and
an integer `extraCandies`, return a boolean array `result` where result[i] is
True if, after giving the i-th kid all `extraCandies`, they would have the
greatest number of candies among all kids (ties count as greatest).

Approach: the current maximum is fixed. Kid i ends up with the greatest count
iff candies[i] + extraCandies >= max(candies). Compute the max once, then test
each kid.

Time:  O(n)
Space: O(n)  (for the output)
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        return [c + extraCandies >= highest for c in candies]


if __name__ == "__main__":
    assert Solution().kidsWithCandies([2, 3, 5, 1, 3], 3) == [True, True, True, False, True]
    assert Solution().kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False]
    assert Solution().kidsWithCandies([12, 1, 12], 10) == [True, False, True]
    print("ok")
