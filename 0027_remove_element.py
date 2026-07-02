"""
27. Remove Element  (Easy)

Remove all occurrences of val from nums in place and return the new length k.
The first k elements must hold the survivors (order doesn't matter); the rest
are ignored.

Approach: a write pointer k. Scan the array and copy every element that isn't
val to nums[k], advancing k. Everything past k is leftover and disregarded.

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    a = [3, 2, 2, 3]
    k = Solution().removeElement(a, 3)
    assert k == 2 and a[:k] == [2, 2]

    b = [0, 1, 2, 2, 3, 0, 4, 2]
    k = Solution().removeElement(b, 2)
    assert k == 5 and b[:k] == [0, 1, 3, 0, 4]

    c = [1]
    assert Solution().removeElement(c, 1) == 0

    d = [4, 5]
    assert Solution().removeElement(d, 9) == 2 and d == [4, 5]
    print("ok")
