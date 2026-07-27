"""
28. Find the Index of the First Occurrence in a String  (Easy)

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
    assert Solution().strStr("abc", "") == 0
    print("ok")
