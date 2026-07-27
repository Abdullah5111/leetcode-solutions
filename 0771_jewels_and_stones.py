"""
771. Jewels and Stones  (Easy)

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
