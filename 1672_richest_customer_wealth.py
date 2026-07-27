"""
1672. Richest Customer Wealth  (Easy)

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
