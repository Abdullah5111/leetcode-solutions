"""
22. Generate Parentheses  (Medium)

Given n pairs of parentheses, generate all combinations of
well-formed parentheses.

Approach: backtracking — add "(" while opens remain, and ")" only
while it would close an open one, so every built string stays valid.

Time:  O(4^n / sqrt(n))  (the n-th Catalan number of results)
Space: O(n) recursion, output excluded
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def build(current: str, opened: int, closed: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return
            if opened < n:
                build(current + "(", opened + 1, closed)
            if closed < opened:
                build(current + ")", opened, closed + 1)

        build("", 0, 0)
        return result


if __name__ == "__main__":
    assert sorted(Solution().generateParenthesis(3)) == sorted(
        ["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert Solution().generateParenthesis(1) == ["()"]
    assert len(Solution().generateParenthesis(4)) == 14
    print("ok")
