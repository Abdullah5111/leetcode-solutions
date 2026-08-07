"""
228. Summary Ranges  (Easy)

Time:  O(n)
Space: O(1)  (ignoring the output)
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i]}")
            i += 1
        return ranges


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([-1]) == ["-1"]
    print("ok")
