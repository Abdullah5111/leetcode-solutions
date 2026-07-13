"""
2798. Number of Employees Who Met the Target  (Easy)

There are n employees, and the i-th employee worked hours[i] hours. The company
requires each employee to work for at least `target` hours. Return the number of
employees who worked at least `target` hours.

Approach: count the elements of `hours` that are >= target in a single pass.

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for h in hours if h >= target)


if __name__ == "__main__":
    assert Solution().numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2) == 3
    assert Solution().numberOfEmployeesWhoMetTarget([5, 1, 4, 2, 2], 6) == 0
    assert Solution().numberOfEmployeesWhoMetTarget([5, 5, 5], 5) == 3
    print("ok")
