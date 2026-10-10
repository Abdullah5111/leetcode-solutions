"""
39. Combination Sum  (Medium)

Given an array of distinct integers candidates and a target, return all
unique combinations where the chosen numbers sum to target. The same
number may be used an unlimited number of times.

Approach: backtracking over sorted candidates — each call may reuse the
current candidate or move on; stop a branch once a candidate overshoots.

Time:  O(n^(t/m))  (t = target, m = smallest candidate)
Space: O(t/m) recursion, output excluded
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def build(start: int, remaining: int, chosen: List[int]) -> None:
            if remaining == 0:
                result.append(chosen[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                chosen.append(candidates[i])
                build(i, remaining - candidates[i], chosen)
                chosen.pop()

        build(0, target, [])
        return result


if __name__ == "__main__":
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert Solution().combinationSum([2], 1) == []
    assert Solution().combinationSum([7, 3, 2], 7) == [[2, 2, 3], [7]]
    print("ok")
