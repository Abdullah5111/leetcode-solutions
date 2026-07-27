"""
2894. Divisible and Non-divisible Sums Difference  (Easy)

Time:  O(n)
Space: O(1)
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(-x if x % m == 0 else x for x in range(1, n + 1))


if __name__ == "__main__":
    assert Solution().differenceOfSums(10, 3) == 19
    assert Solution().differenceOfSums(5, 6) == 15
    assert Solution().differenceOfSums(5, 1) == -15
    assert Solution().differenceOfSums(1, 1) == -1
    print("ok")
