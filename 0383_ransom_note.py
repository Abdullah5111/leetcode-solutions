"""
383. Ransom Note  (Easy)

Time:  O(n + m)  n = len(ransomNote), m = len(magazine)
Space: O(k)  k = distinct characters
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = Counter(magazine)
        for ch in ransomNote:
            if available[ch] == 0:
                return False
            available[ch] -= 1
        return True


if __name__ == "__main__":
    assert Solution().canConstruct("a", "b") is False
    assert Solution().canConstruct("aa", "ab") is False
    assert Solution().canConstruct("aa", "aab") is True
    assert Solution().canConstruct("", "anything") is True
    print("ok")
