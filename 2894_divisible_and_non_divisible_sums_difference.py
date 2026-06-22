"""
2894. Divisible and Non-divisible Sums Difference  (Easy)

Given positive integers n and m, let num1 be the sum of integers in [1, n] that
are NOT divisible by m, and num2 the sum of those that ARE. Return num1 - num2.

Approach: walk 1..n once, adding each value when it isn't a multiple of m and
subtracting it when it is — that single signed sum is exactly num1 - num2.

(Closed form, O(1): total = n(n+1)/2; with k = n // m the divisible sum is
m * k(k+1)/2, and the answer is total - 2 * that.)

Time:  O(n)
Space: O(1)
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return sum(-x if x % m == 0 else x for x in range(1, n + 1))


if __name__ == "__main__":
    assert Solution().differenceOfSums(10, 3) == 19  # divisible: 3,6,9
    assert Solution().differenceOfSums(5, 6) == 15   # none divisible
    assert Solution().differenceOfSums(5, 1) == -15  # all divisible
    assert Solution().differenceOfSums(1, 1) == -1
    print("ok")
