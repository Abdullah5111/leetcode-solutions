"""
322. Coin Change  (Medium)

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of
money. Return the fewest number of coins needed to make up that amount.
If it cannot be made, return -1. You may use each coin unlimited times.

Approach: bottom-up DP — best[a] is the fewest coins for amount a,
built by trying every coin.

Time:  O(amount * len(coins))
Space: O(amount)
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        best = [0] + [INF] * amount
        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    best[a] = min(best[a], best[a - coin] + 1)
        return best[amount] if best[amount] != INF else -1


if __name__ == "__main__":
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3) == -1
    assert Solution().coinChange([1], 0) == 0
    assert Solution().coinChange([186, 419, 83, 408], 6249) == 20
    print("ok")
