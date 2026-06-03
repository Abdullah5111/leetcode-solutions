"""
13. Roman to Integer  (Easy)

Given a Roman numeral string, convert it to an integer. Roman numerals are
normally written largest-to-smallest left-to-right and summed, but six
subtractive pairs (IV, IX, XL, XC, CD, CM) write a smaller symbol before a
larger one to mean "subtract".

Approach: single left-to-right pass. For each symbol, if its value is less
than the value of the symbol to its right, subtract it; otherwise add it.
This handles every subtractive case without special-casing the pairs.

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
