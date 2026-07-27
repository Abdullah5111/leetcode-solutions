"""
242. Valid Anagram  (Easy)

Time:  O(n)
Space: O(1)  (bounded alphabet)
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert Solution().isAnagram("anagram", "nagaram") is True
    assert Solution().isAnagram("rat", "car") is False
    assert Solution().isAnagram("", "") is True
    assert Solution().isAnagram("a", "ab") is False
    assert Solution().isAnagram("ab", "ba") is True
    print("ok")
