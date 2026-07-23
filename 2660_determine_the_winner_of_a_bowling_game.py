"""
2660. Determine the Winner of a Bowling Game  (Easy)

Two players play a turn-based bowling game with the same number of turns.
`player1` and `player2` give the pins knocked down each turn. Scoring: a turn is
normally worth its pin count, but if in either of the previous two turns the
player knocked down all 10 pins, that turn is worth double. Return 1 if player 1
wins, 2 if player 2 wins, or 0 for a draw.

Approach: compute each player's total in a single pass. A turn i is doubled when
turns[i-1] == 10 or turns[i-2] == 10. Sum both totals and compare.

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(turns: List[int]) -> int:
            total = 0
            for i, pins in enumerate(turns):
                bonus = (i >= 1 and turns[i - 1] == 10) or (i >= 2 and turns[i - 2] == 10)
                total += pins * 2 if bonus else pins
            return total

        s1, s2 = score(player1), score(player2)
        if s1 > s2:
            return 1
        if s2 > s1:
            return 2
        return 0


if __name__ == "__main__":
    assert Solution().isWinner([4, 10, 7, 9], [6, 5, 2, 3]) == 1
    assert Solution().isWinner([3, 5, 7, 6], [8, 10, 10, 2]) == 2
    assert Solution().isWinner([2, 3], [4, 1]) == 0
    assert Solution().isWinner([1, 1, 1, 10, 10, 10, 10], [10, 10, 10, 10, 1, 1, 1]) == 2
    print("ok")
