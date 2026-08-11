"""
409. Longest Palindrome  (Easy)

Time:  O(n)
Space: O(k)  k = distinct characters
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        odd_seen = False
        for c in Counter(s).values():
            length += c - (c & 1)
            if c & 1:
                odd_seen = True
        return length + 1 if odd_seen else length


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
    assert Solution().longestPalindrome("a") == 1
    assert Solution().longestPalindrome("bb") == 2
    assert Solution().longestPalindrome("abc") == 1
    print("ok")
