"""
3456. Find Special Substring of Length K  (Easy)

Time:  O(n)
Space: O(1)
"""


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        x = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                x += 1
            else:
                if x == k:
                    return True
                x = 1
        return x == k


if __name__ == "__main__":
    assert Solution().hasSpecialSubstring("aaabaaa", 3) is True
    assert Solution().hasSpecialSubstring("abc", 2) is False
    assert Solution().hasSpecialSubstring("aaaa", 3) is False
    assert Solution().hasSpecialSubstring("a", 1) is True
    assert Solution().hasSpecialSubstring("abbb", 3) is True
    print("ok")
