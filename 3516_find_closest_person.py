"""
3516. Find Closest Person  (Easy)

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
