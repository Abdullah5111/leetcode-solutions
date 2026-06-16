"""
125. Valid Palindrome  (Easy)

A phrase is a palindrome if, after lowercasing and removing every non-
alphanumeric character, it reads the same forwards and backwards. Given a
string s, return True if it is a palindrome.

Approach: two pointers from both ends moving inward. Skip any character that
isn't alphanumeric, then compare the two characters case-insensitively. A
mismatch means it isn't a palindrome. This runs in a single pass with no extra
string allocation.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


if __name__ == "__main__":
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") is True
    assert Solution().isPalindrome("race a car") is False
    assert Solution().isPalindrome(" ") is True  # empty after filtering
    assert Solution().isPalindrome("0P") is False  # '0' vs 'p'
    assert Solution().isPalindrome("ab_a") is True
    print("ok")
