"""
378. Kth Smallest Element in a Sorted Matrix  (Medium)

Given an n x n matrix where each row and each column is sorted in
ascending order, return the k-th smallest element in the matrix.

Approach: binary search on the value range — count how many elements
are <= mid with a staircase scan from the bottom-left corner and
narrow until the count reaches k.

Time:  O(n log(max - min))
Space: O(1)
"""

from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_leq(target: int) -> int:
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= target:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count

        lo, hi = matrix[0][0], matrix[n - 1][n - 1]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_leq(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    assert Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    assert Solution().kthSmallest([[-5]], 1) == -5
    assert Solution().kthSmallest([[1, 2], [1, 3]], 2) == 1
    assert Solution().kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 5) == 7
    print("ok")
