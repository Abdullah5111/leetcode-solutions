"""
807. Max Increase to Keep City Skyline  (Medium)

grid[i][j] is a building's height in an n x n city. You may raise buildings so
that the skyline viewed from the top/bottom (each column's max) and from the
left/right (each row's max) stays unchanged. Return the maximum total height
that can be added.

Approach: a building at (i, j) can rise to at most min(row_max[i], col_max[j])
without poking above either skyline. Precompute each row's and column's max,
then sum the slack for every cell.

Time:  O(n^2)
Space: O(n)
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Skyline as seen along each row (left/right) and each column (top/bottom).
        max_row = [max(row) for row in grid]
        max_col = [max(grid[i][j] for i in range(n)) for j in range(n)]

        total = 0
        for i in range(n):
            for j in range(n):
                # Raise this building to the lower of its two skyline limits.
                total += min(max_row[i], max_col[j]) - grid[i][j]
        return total


if __name__ == "__main__":
    assert Solution().maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    ) == 35
    assert Solution().maxIncreaseKeepingSkyline([[0]]) == 0
    assert Solution().maxIncreaseKeepingSkyline([[1, 2], [3, 4]]) == 1  # (0,0): 1→2
    print("ok")
