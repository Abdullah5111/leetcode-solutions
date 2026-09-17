"""
49. Group Anagrams  (Medium)

Given an array of strings strs, group the anagrams together. Return
the groups in any order.

Approach: hash each word to its sorted-letter key; words sharing a key
are anagrams.

Time:  O(n * k log k)  (k = max word length)
Space: O(n * k)
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[tuple(sorted(word))].append(word)
        return list(groups.values())


if __name__ == "__main__":
    out = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted([sorted(g) for g in out]) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
    print("ok")
