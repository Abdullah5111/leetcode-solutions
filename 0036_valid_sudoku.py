"""
36. Valid Sudoku  (Medium)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated: each row, each column and each of the nine 3 x 3 boxes
must contain the digits 1-9 without repetition. "." marks an empty cell.

Approach: one pass over the board, recording each digit in a set for its
row, its column and its box (box id = (r // 3) * 3 + c // 3). Seeing a
digit already in any of the three sets means the board is invalid.

Time:  O(81) = O(1)
Space: O(81) = O(1)
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    continue
                b = (r // 3) * 3 + c // 3
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    return False
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)
        return True


if __name__ == "__main__":
    valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution().isValidSudoku(valid) is True

    col_clash = [row[:] for row in valid]
    col_clash[0][0] = "8"  # 8 already in column 0 and the top-left box
    assert Solution().isValidSudoku(col_clash) is False

    box_clash = [row[:] for row in valid]
    box_clash[2][0] = "3"  # 3 already in the top-left box only
    assert Solution().isValidSudoku(box_clash) is False

    assert Solution().isValidSudoku([["."] * 9 for _ in range(9)]) is True
    print("ok")
