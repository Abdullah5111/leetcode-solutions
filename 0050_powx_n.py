"""
50. Pow(x, n)  (Medium)

Implement pow(x, n), which calculates x raised to the power n.
n may be negative.

Approach: fast exponentiation — square the base and halve the exponent,
multiplying the result in whenever the current low bit of n is set.
A negative n is x^-1 raised to -n.

Time:  O(log |n|)
Space: O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


if __name__ == "__main__":
    from math import isclose
    assert isclose(Solution().myPow(2.0, 10), 1024.0)
    assert isclose(Solution().myPow(2.1, 3), 9.261)
    assert isclose(Solution().myPow(2.0, -2), 0.25)
    assert Solution().myPow(5.0, 0) == 1.0
    assert Solution().myPow(1.0, -2**31) == 1.0
    assert isclose(Solution().myPow(-2.0, 3), -8.0)
    print("ok")
