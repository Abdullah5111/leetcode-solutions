"""
118. Pascal's Triangle  (Easy)

Given an integer `numRows`, return the first numRows of Pascal's triangle. In
Pascal's triangle, each number is the sum of the two numbers directly above it.

Approach: build the triangle row by row. Each row starts and ends with 1; every
interior entry is the sum of the two adjacent entries in the previous row.

Time:  O(numRows^2)
Space: O(numRows^2)  (for the output)
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle: List[List[int]] = []
        for r in range(numRows):
            row = [1] * (r + 1)
            for c in range(1, r):
                row[c] = triangle[r - 1][c - 1] + triangle[r - 1][c]
            triangle.append(row)
        return triangle


if __name__ == "__main__":
    assert Solution().generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
    assert Solution().generate(1) == [[1]]
    assert Solution().generate(2) == [[1], [1, 1]]
    print("ok")
