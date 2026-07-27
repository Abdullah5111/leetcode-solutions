"""
807. Max Increase to Keep City Skyline  (Medium)

Time:  O(n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = [max(row) for row in grid]
        max_col = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total = 0
        for i in range(n):
            for j in range(n):
                total += min(max_row[i], max_col[j]) - grid[i][j]
        return total


if __name__ == "__main__":
    assert Solution().maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    ) == 35
    assert Solution().maxIncreaseKeepingSkyline([[0]]) == 0
    assert Solution().maxIncreaseKeepingSkyline([[1, 2], [3, 4]]) == 1
    print("ok")
