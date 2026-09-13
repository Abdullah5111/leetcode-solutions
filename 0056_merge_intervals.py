"""
56. Merge Intervals  (Medium)

Given an array of intervals where intervals[i] = [start_i, end_i],
merge all overlapping intervals and return an array of the non-
overlapping intervals that cover all the input intervals.

Approach: sort by start; extend the current interval while the next
one overlaps, otherwise start a new one.

Time:  O(n log n)
Space: O(n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged


if __name__ == "__main__":
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert Solution().merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert Solution().merge([[1, 4], [2, 3]]) == [[1, 4]]
    print("ok")
