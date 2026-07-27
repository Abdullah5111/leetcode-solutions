"""
744. Find Smallest Letter Greater Than Target  (Easy)

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
