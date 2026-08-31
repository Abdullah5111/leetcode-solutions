"""
11. Container With Most Water  (Medium)

You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the i-th line are (i, 0) and
(i, height[i]). Find two lines that together with the x-axis form a
container that holds the most water. Return the maximum amount of water.

Approach: two pointers from both ends; always move the shorter side
inward — the area is limited by it, so only moving it can help.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        l, r = 0, len(height) - 1
        while l < r:
            best = max(best, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best


if __name__ == "__main__":
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea([1, 1]) == 1
    assert Solution().maxArea([4, 3, 2, 1, 4]) == 16
    assert Solution().maxArea([1, 2, 1]) == 2
    print("ok")
