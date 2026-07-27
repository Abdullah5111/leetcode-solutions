"""
121. Best Time to Buy and Sell Stock  (Easy)

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best = 0
        for price in prices:
            min_price = min(min_price, price)
            best = max(best, price - min_price)
        return best


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit([1, 2]) == 1
    assert Solution().maxProfit([3]) == 0
    assert Solution().maxProfit([]) == 0
    print("ok")
