"""
3146. Permutation Difference between Two Strings  (Easy)

Time:  O(n^2)  (t.find per char; n <= 26 so effectively O(1))
Space: O(1)
"""


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        x = 0
        for i, c in enumerate(s):
            idx = t.find(c)
            x += abs(i-idx)
        return x


if __name__ == "__main__":
    assert Solution().findPermutationDifference("abc", "bac") == 2
    assert Solution().findPermutationDifference("abcde", "edbac") == 12
    assert Solution().findPermutationDifference("a", "a") == 0
    print("ok")
