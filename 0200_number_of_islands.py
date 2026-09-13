"""
200. Number of Islands  (Medium)

Given an m x n binary grid where 1 is land and 0 is water, return the
number of islands. An island is surrounded by water and formed by
connecting adjacent lands horizontally or vertically.

Approach: flood fill — scan the grid; each unvisited land cell is a new
island, sink it and its connected land with DFS before counting.

Time:  O(m * n)
Space: O(m * n) worst-case recursion
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def sink(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    sink(r, c)
        return count


if __name__ == "__main__":
    assert Solution().numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1
    assert Solution().numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    assert Solution().numIslands([["1"]]) == 1
    assert Solution().numIslands([["0", "0"]]) == 0
    print("ok")
