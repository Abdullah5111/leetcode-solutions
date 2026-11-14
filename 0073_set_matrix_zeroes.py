"""
73. Set Matrix Zeroes  (Medium)

Given an m x n integer matrix, if an element is 0, set its entire row
and column to 0. Do it in place.

Approach: use the first row and first column as marker storage — a 0 at
matrix[r][0] / matrix[0][c] means "zero this row / column". Two flags
remember whether the first row and first column themselves had a 0,
since their cells get overwritten by markers.

Time:  O(m * n)
Space: O(1)
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = any(matrix[0][c] == 0 for c in range(n))
        first_col = any(matrix[r][0] == 0 for r in range(m))

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row:
            for c in range(n):
                matrix[0][c] = 0
        if first_col:
            for r in range(m):
                matrix[r][0] = 0


if __name__ == "__main__":
    cases = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),  # no zeros
        ([[1, 0]], [[0, 0]]),  # single row
        ([[1], [0], [2]], [[0], [0], [0]]),  # single column
    ]
    for matrix, expected in cases:
        Solution().setZeroes(matrix)
        assert matrix == expected
    print("ok")
