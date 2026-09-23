"""
239. Sliding Window Maximum  (Hard)

You are given an array of integers nums and a sliding window of size k
moving from the leftmost to the rightmost position. Return the maximum
in each window.

Approach: monotonically decreasing deque of indices — the front is
always the current window's max; smaller newcomers pop larger old
values from the back, expired indices fall off the front.

Time:  O(n)
Space: O(k)
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()  # indices, values decreasing
        result = []
        for i, num in enumerate(nums):
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if window[0] <= i - k:
                window.popleft()
            if i >= k - 1:
                result.append(nums[window[0]])
        return result


if __name__ == "__main__":
    assert Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert Solution().maxSlidingWindow([1], 1) == [1]
    assert Solution().maxSlidingWindow([9, 8, 7, 6], 2) == [9, 8, 7]
    assert Solution().maxSlidingWindow([1, 2, 3, 4], 4) == [4]
    print("ok")
