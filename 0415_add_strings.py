"""
415. Add Strings  (Easy)

Time:  O(max(n, m))
Space: O(max(n, m))  (for the output)
"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        digits = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += ord(num1[i]) - ord("0")
                i -= 1
            if j >= 0:
                total += ord(num2[j]) - ord("0")
                j -= 1
            carry, digit = divmod(total, 10)
            digits.append(str(digit))
        return "".join(reversed(digits))


if __name__ == "__main__":
    assert Solution().addStrings("11", "123") == "134"
    assert Solution().addStrings("456", "77") == "533"
    assert Solution().addStrings("0", "0") == "0"
    assert Solution().addStrings("99", "1") == "100"
    print("ok")
