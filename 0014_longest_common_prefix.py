"""
14. Longest Common Prefix  (Easy)

Find the longest common prefix string amongst an array of strings. If there is
no common prefix, return "".

Approach: vertical scanning. Walk character positions left-to-right. For each
position i, take the character from the first string and check that every other
string has the same character there. Stop as soon as a string is too short or
a character differs; the prefix is everything matched so far.

Time:  O(S)   S = total number of characters across all strings (worst case)
Space: O(1)   ignoring the output
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first = strs[0]
        for i, ch in enumerate(first):
            for other in strs[1:]:
                if i >= len(other) or other[i] != ch:
                    return first[:i]
        return first


if __name__ == "__main__":
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert Solution().longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"
    assert Solution().longestCommonPrefix(["a"]) == "a"
    assert Solution().longestCommonPrefix(["", "abc"]) == ""
    print("ok")
