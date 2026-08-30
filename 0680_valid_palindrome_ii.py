"""
680. Valid Palindrome II  (Easy)

Given a string s, return true if s can be a palindrome after deleting
at most one character from it.

Approach: two pointers; on the first mismatch, check whether skipping
either the left or the right character leaves a palindrome.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    assert Solution().validPalindrome("aba") is True
    assert Solution().validPalindrome("abca") is True
    assert Solution().validPalindrome("abc") is False
    assert Solution().validPalindrome("cbbcc") is True
    assert Solution().validPalindrome("deeee") is True
    print("ok")
