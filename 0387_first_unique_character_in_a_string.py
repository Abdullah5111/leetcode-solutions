"""
387. First Unique Character in a String  (Easy)

Time:  O(n)
Space: O(k)  k = distinct characters
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1


if __name__ == "__main__":
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
    assert Solution().firstUniqChar("aabb") == -1
    assert Solution().firstUniqChar("z") == 0
    print("ok")
