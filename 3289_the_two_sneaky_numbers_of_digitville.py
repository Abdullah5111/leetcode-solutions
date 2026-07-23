"""
3289. The Two Sneaky Numbers of Digitville  (Easy)

In Digitville a list `nums` was meant to contain every integer from 0 to n-1
exactly once, but two of those numbers appear twice, making the list length
n+2. Return the two numbers that appear twice, in any order.

Approach: count occurrences of each value; the two values seen more than once
are the sneaky numbers. A set of already-seen values works too: the second time
we encounter a value it is a duplicate.

Time:  O(n)
Space: O(n)
"""
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for n in nums:
            if n in seen:
                result.append(n)
            else:
                seen.add(n)
        return result


if __name__ == "__main__":
    assert sorted(Solution().getSneakyNumbers([0, 1, 1, 0])) == [0, 1]
    assert sorted(Solution().getSneakyNumbers([0, 3, 2, 1, 3, 2])) == [2, 3]
    assert sorted(Solution().getSneakyNumbers([7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2])) == [4, 5]
    print("ok")
