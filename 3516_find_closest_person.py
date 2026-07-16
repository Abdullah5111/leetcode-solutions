"""
3516. Find Closest Person  (Easy)

You are given three integers `x`, `y`, and `z` representing the positions of
three people on a number line: person 1 at x, person 2 at y, and a target at z.
Persons 1 and 2 move toward the target at the same speed. Return 1 if person 1
arrives first, 2 if person 2 arrives first, or 0 if they arrive at the same time.

Approach: arrival time is proportional to distance from the target, |x - z| and
|y - z|. Compare the two distances and report whichever is smaller (0 on a tie).

Time:  O(1)
Space: O(1)
"""


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) < abs(y - z):
            return 1
        if abs(x - z) > abs(y - z):
            return 2
        return 0


if __name__ == "__main__":
    assert Solution().findClosest(2, 7, 4) == 1
    assert Solution().findClosest(2, 5, 6) == 2
    assert Solution().findClosest(1, 5, 3) == 0
    print("ok")
