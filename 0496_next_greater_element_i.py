"""
496. Next Greater Element I  (Easy)

Time:  O(n + m)
Space: O(m)
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                next_greater[stack.pop()] = x
            stack.append(x)
        return [next_greater.get(x, -1) for x in nums1]


if __name__ == "__main__":
    assert Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert Solution().nextGreaterElement([1], [1]) == [-1]
    print("ok")
