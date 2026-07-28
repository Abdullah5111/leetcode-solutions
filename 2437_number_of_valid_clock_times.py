"""
2437. Number of Valid Clock Times  (Easy)

Time:  O(1)
Space: O(1)
"""


class Solution:
    def countTime(self, time: str) -> int:
        def count(pattern: str, limit: int) -> int:
            total = 0
            for value in range(limit + 1):
                digits = f"{value:02d}"
                if pattern[0] in ("?", digits[0]) and pattern[1] in ("?", digits[1]):
                    total += 1
            return total

        return count(time[:2], 23) * count(time[3:], 59)


if __name__ == "__main__":
    assert Solution().countTime("?5:00") == 2
    assert Solution().countTime("0?:0?") == 100
    assert Solution().countTime("??:??") == 1440
    assert Solution().countTime("2?:22") == 4
    assert Solution().countTime("12:34") == 1
    print("ok")
