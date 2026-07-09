"""
771. Jewels and Stones  (Easy)

You are given `jewels` representing the types of stones that are jewels, and
`stones` representing the stones you have. Each character in `stones` is a type
of stone you have. Return how many of the stones you have are also jewels.
Letters are case sensitive.

Approach: put the jewel types into a set for O(1) membership checks, then count
how many characters of `stones` are in that set.

Time:  O(n + m)  where n = len(jewels), m = len(stones)
Space: O(n)
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        return sum(1 for s in stones if s in jewel_set)


if __name__ == "__main__":
    assert Solution().numJewelsInStones("aA", "aAAbbbb") == 3
    assert Solution().numJewelsInStones("z", "ZZ") == 0
    assert Solution().numJewelsInStones("", "abc") == 0
    assert Solution().numJewelsInStones("abc", "") == 0
    print("ok")
