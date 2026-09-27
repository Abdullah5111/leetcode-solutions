"""
74. Search a 2D Matrix  (Medium)

You are given an m x n integer matrix where each row is sorted and the
first integer of each row is greater than the last integer of the
previous row. Return true if target is in the matrix. Must run in
O(log(m * n)) time.

Approach: treat the matrix as one flattened sorted array and binary
search it, mapping index k to matrix[k // n][k % n].

Time:  O(log(m * n))
Space: O(1)
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert Solution().searchMatrix(matrix, 3) is True
    assert Solution().searchMatrix(matrix, 13) is False
    assert Solution().searchMatrix(matrix, 60) is True
    assert Solution().searchMatrix([[1]], 0) is False
    assert Solution().searchMatrix([[1], [3]], 3) is True
    print("ok")
