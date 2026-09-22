"""
42. Trapping Rain Water  (Hard)

Given n non-negative integers representing an elevation map where the
width of each bar is 1, compute how much water it can trap after raining.

Approach: two pointers — water above a bar is bounded by the smaller
of the best wall seen on each side; moving the side with the lower
max is always safe because the other side already has a taller wall.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        while l < r:
            if height[l] <= height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
        return water


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    assert Solution().trap([1, 2, 3, 4]) == 0
    assert Solution().trap([]) == 0
    assert Solution().trap([5]) == 0
    print("ok")
