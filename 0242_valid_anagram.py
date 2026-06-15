"""
242. Valid Anagram  (Easy)

Given two strings s and t, return True if t is an anagram of s, and False
otherwise. An anagram uses exactly the same characters with the same counts,
just reordered.

Approach: two strings are anagrams iff their character-frequency maps are equal.
Build a count for each string and compare. A quick length check short-circuits
the common mismatch. Counting is O(n) and the comparison is over at most 26
keys for lowercase input.

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
