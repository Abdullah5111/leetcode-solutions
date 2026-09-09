"""
347. Top K Frequent Elements  (Medium)

Given an integer array nums and an integer k, return the k most
frequent elements. The answer is guaranteed to be unique. The
algorithm must be better than O(n log n).

Approach: count frequencies, bucket by count (a value's bucket index
is its frequency, bounded by n), then walk buckets from high to low.

Time:  O(n)
Space: O(n)
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        ans = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans


if __name__ == "__main__":
    assert sorted(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert Solution().topKFrequent([1], 1) == [1]
    assert sorted(Solution().topKFrequent([4, 4, 4, 6, 6, 7], 1)) == [4]
    assert sorted(Solution().topKFrequent([1, 2], 2)) == [1, 2]
    print("ok")
