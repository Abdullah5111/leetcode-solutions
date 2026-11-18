"""
64. Minimum Path Sum  (Medium)

Given an m x n grid of non-negative numbers, find a path from the
top-left to the bottom-right which minimizes the sum of all numbers
along it. You can only move right or down.

Approach: 1-D DP over one row — dp[c] holds the cheapest cost to reach
column c of the current row. Each cell is reached from above (dp[c],
still the previous row's value) or from the left (dp[c - 1], already
updated for this row).

Time:  O(m * n)
Space: O(n)
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dp = [float("inf")] * n
        dp[0] = 0
        for row in grid:
            dp[0] += row[0]
            for c in range(1, n):
                dp[c] = min(dp[c], dp[c - 1]) + row[c]
        return dp[-1]


if __name__ == "__main__":
    assert Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert Solution().minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    assert Solution().minPathSum([[5]]) == 5
    assert Solution().minPathSum([[1, 2, 3]]) == 6  # single row
    assert Solution().minPathSum([[1], [2], [3]]) == 6  # single column
    print("ok")
