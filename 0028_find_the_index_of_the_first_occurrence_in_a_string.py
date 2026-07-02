"""
28. Find the Index of the First Occurrence in a String  (Easy)

Return the index of the first occurrence of needle in haystack, or -1 if it
isn't present. (An empty needle matches at index 0.)

Approach: try each start position i where needle could still fit and compare the
window haystack[i:i+m] against needle. Straightforward O(n*m) scan — fine for the
constraints; KMP would make it O(n+m) if needed.

Time:  O(n*m)
Space: O(1)  (ignoring the slice made for comparison)
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().strStr("sadbutsad", "sad") == 0
    assert Solution().strStr("leetcode", "leeto") == -1
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("a", "a") == 0
    assert Solution().strStr("abc", "") == 0  # empty needle matches at 0
    print("ok")
