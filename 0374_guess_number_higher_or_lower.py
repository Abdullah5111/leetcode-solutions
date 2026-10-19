"""
374. Guess Number Higher or Lower  (Easy)

A number is picked from 1 to n. Calling guess(num) returns -1 if num is
higher than the pick, 1 if num is lower, and 0 if it is correct.
Return the picked number.

Approach: binary search over [lo, hi] — each answer halves the range
that can still contain the pick.

Time:  O(log n)
Space: O(1)
"""

# LeetCode provides guess(); this stand-in lets the file run locally.
_pick = 0
_calls = 0


def guess(num: int) -> int:
    global _calls
    _calls += 1
    if num > _pick:
        return -1
    if num < _pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:    # pick is higher than mid
                lo = mid + 1
            else:           # pick is lower than mid
                hi = mid - 1


if __name__ == "__main__":
    for n, pick in [(10, 6), (1, 1), (2, 1), (2, 2), (1000, 700),
                    (2**31 - 1, 1702766719), (2**31 - 1, 2**31 - 1), (2**31 - 1, 1)]:
        _pick, _calls = pick, 0
        assert Solution().guessNumber(n) == pick
        assert _calls <= 32
    print("ok")
