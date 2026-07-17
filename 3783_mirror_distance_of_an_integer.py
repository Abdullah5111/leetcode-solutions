"""
3783. Mirror Distance of an Integer  (Easy)

The mirror distance of an integer n is defined as abs(n - reverse(n)), where
reverse(n) is the integer formed by reversing the digits of n (leading zeros in
the reversed number are omitted). Given an integer n, return its mirror
distance.

Approach: build the reversed number arithmetically. Starting from y = 0,
repeatedly take the last digit of x (x % 10), append it to y (y * 10 + digit),
and drop it from x (x //= 10) until x is 0. Dropping trailing zeros of n this
way naturally omits the leading zeros of the reverse (e.g. 10 -> 1). The answer
is abs(n - y).

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
