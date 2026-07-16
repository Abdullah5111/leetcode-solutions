"""
744. Find Smallest Letter Greater Than Target  (Easy)

You are given an array of characters `letters` that is sorted in non-decreasing
order, and a character `target`. Return the smallest character in `letters` that
is lexicographically greater than `target`. If no such character exists, the
letters wrap around, so return letters[0].

Approach: because `letters` is sorted, binary search for the insertion point of
the smallest character strictly greater than `target`. Narrow [lo, hi) until lo
points at the first letter > target; take it modulo len(letters) to handle the
wrap-around when target is >= every letter.

Time:  O(log n)
Space: O(1)
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo, hi = 0, len(letters)
        while lo < hi:
            mid = (lo + hi) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return letters[lo % len(letters)]


if __name__ == "__main__":
    assert Solution().nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "j") == "c"
    assert Solution().nextGreatestLetter(["x", "x", "y", "y"], "z") == "x"
    assert Solution().nextGreatestLetter(["a", "b"], "a") == "b"
    print("ok")
