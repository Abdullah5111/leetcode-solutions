"""
191. Number of 1 Bits  (Easy)

Time:  O(k)  k = number of set bits
Space: O(1)
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    assert Solution().hammingWeight(11) == 3
    assert Solution().hammingWeight(128) == 1
    assert Solution().hammingWeight(2147483645) == 30
    assert Solution().hammingWeight(0) == 0
    print("ok")
