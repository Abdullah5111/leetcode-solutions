"""
1967. Number of Strings That Appear as Substrings in Word  (Easy)

Time:  O(m * n * k)  where m = len(patterns), n = len(word), k = avg pattern len
Space: O(1)
"""

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for p in patterns if p in word)


if __name__ == "__main__":
    assert Solution().numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
    assert Solution().numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
    assert Solution().numOfStrings(["a", "a", "a"], "ab") == 3
    assert Solution().numOfStrings(["xyz"], "ab") == 0
    print("ok")
