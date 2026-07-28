"""
3751. Total Waviness of Numbers in Range I  (Medium)

Time:  O((num2 - num1) * d)  d = number of digits (<= 6 for num <= 10^5)
Space: O(1)
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(x: int) -> int:
            d = str(x)
            w = 0
            for i in range(1, len(d) - 1):
                if d[i] > d[i - 1] and d[i] > d[i + 1]:
                    w += 1
                elif d[i] < d[i - 1] and d[i] < d[i + 1]:
                    w += 1
            return w

        return sum(waviness(x) for x in range(num1, num2 + 1))


if __name__ == "__main__":
    assert Solution().totalWaviness(120, 130) == 3
    assert Solution().totalWaviness(198, 202) == 3
    assert Solution().totalWaviness(4848, 4848) == 2
    assert Solution().totalWaviness(1, 99) == 0
    print("ok")
