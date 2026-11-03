"""
1128. Number of Equivalent Domino Pairs  (Easy)

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to
dominoes[j] = [c, d] if (a == c and b == d) or (a == d and b == c).
Return the number of pairs (i, j) with i < j that are equivalent.

Approach: normalize each domino so the smaller value comes first, then
encode it as a two-digit number (values are 1..9) and count in a
100-slot array. A bucket of size c contributes c * (c - 1) / 2 pairs.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        x = [0] * 100
        n = len(dominoes)

        for d in dominoes:
            a = min(d)
            b = max(d)
            idx = b*10 + a
            x[idx] += 1

        ans = 0
        for i in range(100):
            ans += (x[i]*(x[i]-1)) // 2
        return ans


if __name__ == "__main__":
    assert Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
    assert Solution().numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3
    assert Solution().numEquivDominoPairs([[1, 1]]) == 0
    assert Solution().numEquivDominoPairs([[9, 9], [9, 9], [9, 9]]) == 3
    print("ok")
