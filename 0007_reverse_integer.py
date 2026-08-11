"""
7. Reverse Integer  (Medium)

Time:  O(log x)
Space: O(1)
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        return rev if -(2 ** 31) <= rev <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(0) == 0
    print("ok")
