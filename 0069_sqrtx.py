"""
69. Sqrt(x)  (Easy)

Given a non-negative integer x, return the square root of x rounded
down to the nearest integer, without using any built-in exponent
function or operator.

Approach: binary search for the largest m with m * m <= x.

Time:  O(log x)
Space: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid - 1
        return lo


if __name__ == "__main__":
    from math import isqrt
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(0) == 0
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(2**31 - 1) == 46340
    assert all(Solution().mySqrt(x) == isqrt(x) for x in range(2000))
    print("ok")
