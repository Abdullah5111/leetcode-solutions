"""
3760. Maximum Substrings With Distinct Start  (Medium)

Time:  O(n)
Space: O(1)  (at most 26 distinct letters)
"""

class Solution:
    def maxSubstrings(self, s: str) -> int:
        return len(set(s))


if __name__ == "__main__":
    assert Solution().maxSubstrings("abab") == 2
    assert Solution().maxSubstrings("abcd") == 4
    assert Solution().maxSubstrings("aaaa") == 1
    assert Solution().maxSubstrings("aab") == 2
    assert Solution().maxSubstrings("z") == 1
    print("ok")
