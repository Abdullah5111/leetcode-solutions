"""
79. Word Search  (Medium)

Given an m x n grid of characters and a string word, return true if
word exists in the grid. The word is built from sequentially adjacent
(horizontal or vertical) cells; a cell may not be used more than once.

Approach: DFS backtracking from every cell — mark a cell as visited
while exploring from it, then restore it on the way back.

Time:  O(m * n * 3^L)  (L = word length)
Space: O(L) recursion
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1)
                     or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return found

        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert Solution().exist(board, "ABCCED") is True
    assert Solution().exist(board, "SEE") is True
    assert Solution().exist(board, "ABCB") is False
    assert Solution().exist([["a"]], "a") is True
    assert Solution().exist([["a", "a"]], "aaa") is False
    print("ok")
