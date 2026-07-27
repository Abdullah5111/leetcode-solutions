"""
2011. Final Value of Variable After Performing Operations  (Easy)

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
