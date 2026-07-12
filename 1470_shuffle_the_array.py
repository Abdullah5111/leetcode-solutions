"""
1470. Shuffle the Array  (Easy)

Given the array `nums` consisting of 2n elements in the form
[x1, x2, ..., xn, y1, y2, ..., yn], return the array in the form
[x1, y1, x2, y2, ..., xn, yn].

Approach: the first half holds the x values (indices 0..n-1) and the second half
the y values (indices n..2n-1). Interleave them by walking i from 0 to n-1 and
appending nums[i] then nums[i + n].

Time:  O(n)
Space: O(n)  (for the output)
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])
        return result


if __name__ == "__main__":
    assert Solution().shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
    assert Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
    assert Solution().shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
    print("ok")
