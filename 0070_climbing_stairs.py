"""
70. Climbing Stairs  (Easy)

Time:  O(n)
Space: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
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
