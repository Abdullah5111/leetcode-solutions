"""
62. Unique Paths  (Medium)

A robot on an m x n grid starts at the top-left corner and can only
move right or down. Return the number of unique paths to the
bottom-right corner.

Approach: DP with a single row — each cell's count is the cell above
(previous row value) plus the cell to the left.

Time:  O(m * n)
Space: O(n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


if __name__ == "__main__":
    assert Solution().uniquePaths(3, 7) == 28
    assert Solution().uniquePaths(3, 2) == 3
    assert Solution().uniquePaths(1, 1) == 1
    assert Solution().uniquePaths(1, 5) == 1
    assert Solution().uniquePaths(10, 10) == 48620
    print("ok")
