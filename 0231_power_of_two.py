"""
231. Power of Two  (Easy)

Time:  O(1)
Space: O(1)
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


if __name__ == "__main__":
    assert Solution().isPowerOfTwo(1) is True
    assert Solution().isPowerOfTwo(16) is True
    assert Solution().isPowerOfTwo(3) is False
    assert Solution().isPowerOfTwo(0) is False
    assert Solution().isPowerOfTwo(-16) is False
    print("ok")
