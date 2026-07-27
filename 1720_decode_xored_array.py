"""
1720. Decode XORed Array  (Easy)

Time:  O(n)
Space: O(n)  (for the output)
"""

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr


if __name__ == "__main__":
    assert Solution().decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert Solution().decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
    assert Solution().decode([], 5) == [5]
    print("ok")
