"""
13. Roman to Integer  (Easy)

Time:  O(n)   n = length of the string
Space: O(1)   the value map is fixed size
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
        }
        total = 0
        for i, ch in enumerate(s):
            if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
                total -= values[ch]
            else:
                total += values[ch]
        return total


if __name__ == "__main__":
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("IV") == 4
    assert Solution().romanToInt("IX") == 9
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
    print("ok")
