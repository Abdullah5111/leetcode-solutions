"""
392. Is Subsequence  (Easy)

Time:  O(n)  n = len(t)
Space: O(1)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


if __name__ == "__main__":
    assert Solution().isSubsequence("abc", "ahbgdc") is True
    assert Solution().isSubsequence("axc", "ahbgdc") is False
    assert Solution().isSubsequence("", "anything") is True
    assert Solution().isSubsequence("abc", "") is False
    print("ok")
