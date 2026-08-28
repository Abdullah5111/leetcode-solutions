"""
605. Can Place Flowers  (Easy)

You have a long flowerbed where some plots are planted and some are not.
However, flowers cannot be planted in adjacent plots. Given an integer
array flowerbed (0 = empty, 1 = planted) and an integer n, return true
if n new flowers can be planted in it without violating the
no-adjacent-flowers rule.

Approach: scan left to right; a plot is plantable when it and both
neighbors are empty. Plant greedily and count.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if (flowerbed[i] == 0
                    and (i == 0 or flowerbed[i - 1] == 0)
                    and (i == length - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                count += 1
        return count >= n


if __name__ == "__main__":
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) is True
    assert Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) is False
    assert Solution().canPlaceFlowers([0], 1) is True
    assert Solution().canPlaceFlowers([1, 0], 1) is False
    assert Solution().canPlaceFlowers([0, 0, 0], 2) is True
    print("ok")
