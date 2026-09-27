"""
15. 3Sum  (Medium)

Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i, j, k are distinct and nums[i] + nums[j] + nums[k]
== 0. The solution set must not contain duplicate triplets.

Approach: sort, fix each first element, then two-pointer the rest;
skip equal neighbors to avoid duplicate triplets.

Time:  O(n^2)
Space: O(1) extra (output and sort excluded)
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans


if __name__ == "__main__":
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0, 1, 1]) == []
    assert Solution().threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert Solution().threeSum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    print("ok")
