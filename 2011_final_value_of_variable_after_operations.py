"""
2011. Final Value of Variable After Performing Operations  (Easy)

There is a variable X starting at 0. You are given an array of strings
`operations`, each being one of "++X", "X++", "--X", or "X--". "++X" and "X++"
increment X by 1; "--X" and "X--" decrement X by 1. Return the final value of X.

Approach: each operation moves X by exactly +1 or -1. The direction is decided
by whether the operation contains a '+' or a '-'. Sum the deltas.

Time:  O(n)
Space: O(1)
"""
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return sum(1 if "+" in op else -1 for op in operations)


if __name__ == "__main__":
    assert Solution().finalValueAfterOperations(["--X", "X++", "X++"]) == 1
    assert Solution().finalValueAfterOperations(["++X", "++X", "X++"]) == 3
    assert Solution().finalValueAfterOperations(["X++", "++X", "--X", "X--"]) == 0
    assert Solution().finalValueAfterOperations([]) == 0
    print("ok")
