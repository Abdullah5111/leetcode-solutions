"""
5. Longest Palindromic Substring  (Medium)

Given a string s, return the longest palindromic substring in s.

Approach: expand around center — every palindrome mirrors around either
a single char (odd length) or a gap between two chars (even length).
Try all 2n - 1 centers and keep the widest expansion.

Time:  O(n^2)
Space: O(1)
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lo: int, hi: int) -> tuple:
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi

        start = end = 0
        for i in range(len(s)):
            for lo, hi in (expand(i, i), expand(i, i + 1)):
                if hi - lo > end - start:
                    start, end = lo, hi
        return s[start:end]


if __name__ == "__main__":
    assert Solution().longestPalindrome("babad") in ("bab", "aba")
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("a") == "a"
    assert Solution().longestPalindrome("forgeeksskeegfor") == "geeksskeeg"
    assert Solution().longestPalindrome("abcd") == "a"
    print("ok")
