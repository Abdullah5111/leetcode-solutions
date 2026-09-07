"""
338. Counting Bits  (Easy)

Given an integer n, return an array ans of length n + 1 such that for
each i (0 <= i <= n), ans[i] is the number of 1's in the binary
representation of i. Solve it in O(n) with a single pass.

Approach: DP — the count for i is the count of i shifted right by one
plus its lowest bit (ans[i] = ans[i >> 1] + (i & 1)).

Time:  O(n)
Space: O(1) extra (output excluded)
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    assert Solution().countBits(2) == [0, 1, 1]
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
    assert Solution().countBits(0) == [0]
    assert Solution().countBits(1) == [0, 1]
    print("ok")
