"""
70. Climbing Stairs  (Easy)

You climb a staircase of n steps, taking either 1 or 2 steps at a time. Return
the number of distinct ways to reach the top.

Approach: the ways to reach step i equal the ways to reach i-1 (then a single
step) plus the ways to reach i-2 (then a double step) — the Fibonacci
recurrence. Iterate bottom-up keeping only the last two values.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1  # ways to reach step 0 and step 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == "__main__":
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8
    assert Solution().climbStairs(10) == 89
    print("ok")
