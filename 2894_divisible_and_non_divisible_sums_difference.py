"""
2894. Divisible and Non-divisible Sums Difference  (Easy)

Time:  O(1)
Space: O(1)
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n + 1) // 2
        k = n // m
        divisible = m * k * (k + 1) // 2
        return total - 2 * divisible


if __name__ == "__main__":
    assert Solution().differenceOfSums(10, 3) == 19
    assert Solution().differenceOfSums(5, 6) == 15
    assert Solution().differenceOfSums(5, 1) == -15
    assert Solution().differenceOfSums(1, 1) == -1
    print("ok")
