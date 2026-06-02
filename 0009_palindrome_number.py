"""
9. Palindrome Number  (Easy)

Given an integer x, return True if x is a palindrome (reads the same forwards
and backwards). Negative numbers are not palindromes ('-' breaks symmetry).

Approach: reverse only half the digits, then compare.
- Any negative number, or any positive number ending in 0 (except 0 itself),
  cannot be a palindrome.
- Otherwise, peel digits off the right of x and build them onto `rev`. Stop
  when rev >= x; at that point we've consumed at least half the digits.
- For even-length numbers, x == rev. For odd-length, x == rev // 10
  (the middle digit doesn't need to match itself).

Avoids converting to a string and avoids potential overflow from fully
reversing the integer.

Time:  O(log10(x))
Space: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


if __name__ == "__main__":
    assert Solution().isPalindrome(121) is True
    assert Solution().isPalindrome(-121) is False
    assert Solution().isPalindrome(10) is False
    assert Solution().isPalindrome(0) is True
    assert Solution().isPalindrome(12321) is True
    assert Solution().isPalindrome(1221) is True
    print("ok")
