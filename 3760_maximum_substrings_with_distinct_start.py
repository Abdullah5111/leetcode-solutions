"""
3760. Maximum Substrings With Distinct Start  (Medium)

Given a string `s` of lowercase English letters, split it into contiguous
substrings so that no two substrings start with the same character. Return the
maximum number of substrings such a split can produce.

Approach: every substring contributes exactly one starting character, and those
starting characters must be distinct, so the number of substrings can never
exceed the number of distinct characters in `s`. That bound is always
achievable: scan left to right and cut a new substring at the first occurrence
of each new character, letting repeats fall inside the current substring. Hence
the answer is simply the count of distinct characters in `s`.

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
