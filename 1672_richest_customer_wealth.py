"""
1672. Richest Customer Wealth  (Easy)

You are given an m x n grid `accounts` where accounts[i][j] is the amount of
money the i-th customer has in the j-th bank. A customer's wealth is the sum of
their bank account balances. Return the wealth of the richest customer.

Approach: each row is one customer, so their wealth is the row sum. Take the
maximum row sum across all customers.

Time:  O(m * n)
Space: O(1)
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer) for customer in accounts)


if __name__ == "__main__":
    assert Solution().maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert Solution().maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert Solution().maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    assert Solution().maximumWealth([[5]]) == 5
    print("ok")
