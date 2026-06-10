"""
121. Best Time to Buy and Sell Stock  (Easy)

Given prices where prices[i] is the price of a stock on day i, choose one day
to buy and a later day to sell. Return the maximum profit, or 0 if no profit
is possible.

Approach: scan once, tracking the lowest price seen so far. On each day the
best profit ending today is price - min_so_far; keep the running maximum. A
single pass suffices because buying always happens at the cheapest earlier day.

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
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5  # buy at 1, sell at 6
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0  # only decreasing
    assert Solution().maxProfit([1, 2]) == 1
    assert Solution().maxProfit([3]) == 0
    assert Solution().maxProfit([]) == 0
    print("ok")
