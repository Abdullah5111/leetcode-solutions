"""
3783. Mirror Distance of an Integer  (Easy)

Time:  O(log n)
Space: O(1)
"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        x, y = n, 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        return abs(n - y)


if __name__ == "__main__":
    assert Solution().mirrorDistance(25) == 27
    assert Solution().mirrorDistance(10) == 9
    assert Solution().mirrorDistance(7) == 0
    assert Solution().mirrorDistance(121) == 0
    assert Solution().mirrorDistance(1200) == 1179
    print("ok")
