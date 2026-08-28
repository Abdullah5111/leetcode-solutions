"""
509. Fibonacci Number  (Easy)

The Fibonacci numbers, commonly denoted F(n), form a sequence such that
F(0) = 0, F(1) = 1 and F(n) = F(n - 1) + F(n - 2) for n > 1.
Given n, calculate F(n).

Approach: iterate with two rolling values.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    assert Solution().fib(2) == 1
    assert Solution().fib(3) == 2
    assert Solution().fib(4) == 3
    assert Solution().fib(0) == 0
    assert Solution().fib(1) == 1
    print("ok")
