"""
2180. Count Integers With Even Digit Sum  (Easy)

Time:  O(num * d)  d = number of digits
Space: O(1)
"""


class Solution:
    def countEven(self, num: int) -> int:
        def digit_sum(x: int) -> int:
            total = 0
            while x:
                total += x % 10
                x //= 10
            return total

        return sum(1 for x in range(1, num + 1) if digit_sum(x) % 2 == 0)


if __name__ == "__main__":
    assert Solution().countEven(4) == 2
    assert Solution().countEven(30) == 14
    assert Solution().countEven(1) == 0
    assert Solution().countEven(2) == 1
    print("ok")
