"""
9. Palindrome Number  (Easy)

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
