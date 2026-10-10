"""
17. Letter Combinations of a Phone Number  (Medium)

Given a string of digits 2-9, return all possible letter combinations
the number could represent on a phone keypad. Return [] for "".

Approach: build combinations digit by digit — extend every partial
string with each letter of the next digit.

Time:  O(4^n * n)
Space: O(4^n * n) output
"""

from typing import List

KEYPAD = {
    "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
    "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combos = [""]
        for digit in digits:
            combos = [prefix + letter for prefix in combos for letter in KEYPAD[digit]]
        return combos


if __name__ == "__main__":
    assert Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert Solution().letterCombinations("") == []
    assert Solution().letterCombinations("2") == ["a", "b", "c"]
    assert len(Solution().letterCombinations("79")) == 16
    print("ok")
