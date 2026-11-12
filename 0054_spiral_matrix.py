"""
54. Spiral Matrix  (Medium)

Given an m x n matrix, return all elements of the matrix in spiral
order (clockwise, starting from the top-left).

Approach: shrink four boundaries — walk the top row, right column,
bottom row (if a row is still left) and left column (if a column is
still left), tightening each boundary after walking it.

Time:  O(m * n)
Space: O(1) extra (output aside)
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                out.append(matrix[top][c])
            top += 1
            for r in range(top, bottom + 1):
                out.append(matrix[r][right])
            right -= 1
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    out.append(matrix[bottom][c])
                bottom -= 1
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    out.append(matrix[r][left])
                left += 1
        return out


if __name__ == "__main__":
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert Solution().spiralOrder([[1, 2, 3]]) == [1, 2, 3]  # single row
    assert Solution().spiralOrder([[1], [2], [3]]) == [1, 2, 3]  # single column
    assert Solution().spiralOrder([[7]]) == [7]
    print("ok")
