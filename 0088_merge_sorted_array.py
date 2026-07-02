"""
88. Merge Sorted Array  (Easy)

nums1 has length m + n: its first m slots are sorted values and the last n are
zero padding. nums2 holds n sorted values. Merge nums2 into nums1 in place so
nums1 becomes one sorted array. Return nothing (mutate nums1).

Approach: fill nums1 from the back. Compare the largest unmerged element of each
side (i in nums1, j in nums2) and drop the bigger into the tail position k,
walking all three pointers left. Writing back-to-front means we never overwrite
an nums1 value we still need to read.

Time:  O(m + n)
Space: O(1)
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    Solution().merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]

    b = [1]
    Solution().merge(b, 1, [], 0)
    assert b == [1]

    c = [0]
    Solution().merge(c, 0, [1], 1)
    assert c == [1]

    d = [4, 5, 6, 0, 0, 0]
    Solution().merge(d, 3, [1, 2, 3], 3)
    assert d == [1, 2, 3, 4, 5, 6]
    print("ok")
