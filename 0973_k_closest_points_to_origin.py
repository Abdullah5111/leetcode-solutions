"""
973. K Closest Points to Origin  (Medium)

Given an array of points [x, y] and an integer k, return the k points
closest to the origin (0, 0) by Euclidean distance, in any order.

Approach: heapq.nsmallest keyed on squared distance — no square root
needed since it preserves order, and the heap keeps only k items.

Time:  O(n log k)
Space: O(k)
"""

from heapq import nsmallest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])


if __name__ == "__main__":
    assert Solution().kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    assert Solution().kClosest([[0, 1]], 1) == [[0, 1]]
    assert sorted(Solution().kClosest([[1, 1], [2, 2], [3, 3]], 3)) == [[1, 1], [2, 2], [3, 3]]
    print("ok")
