"""
28. Find the Index of the First Occurrence in a String  (Easy)

Time:  O(n + m)  KMP: build the prefix table, then one pass over the haystack
Space: O(m)  for the prefix table
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        if m == 0:
            return 0

        lps = [0] * m
        k = 0
        for i in range(1, m):
            while k and needle[i] != needle[k]:
                k = lps[k - 1]
            if needle[i] == needle[k]:
                k += 1
            lps[i] = k

        k = 0
        for i, ch in enumerate(haystack):
            while k and ch != needle[k]:
                k = lps[k - 1]
            if ch == needle[k]:
                k += 1
            if k == m:
                return i - m + 1
        return -1


if __name__ == "__main__":
    assert Solution().strStr("sadbutsad", "sad") == 0
    assert Solution().strStr("leetcode", "leeto") == -1
    assert Solution().strStr("hello", "ll") == 2
    assert Solution().strStr("a", "a") == 0
    assert Solution().strStr("abc", "") == 0
    print("ok")
