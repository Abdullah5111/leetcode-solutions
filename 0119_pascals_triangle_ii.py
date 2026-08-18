"""
119. Pascal's Triangle II  (Easy)

Time:  O(k^2)
Space: O(k)  (single row, updated in place)
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == "__main__":
    assert Solution().getRow(3) == [1, 3, 3, 1]
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1, 1]
    assert Solution().getRow(4) == [1, 4, 6, 4, 1]
    print("ok")
