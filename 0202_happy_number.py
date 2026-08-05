"""
202. Happy Number  (Easy)

Time:  O(log n) per step, until a cycle or 1 is reached
Space: O(k)  k = distinct values visited
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1


if __name__ == "__main__":
    assert Solution().isHappy(19) is True
    assert Solution().isHappy(2) is False
    assert Solution().isHappy(1) is True
    assert Solution().isHappy(7) is True
    print("ok")
