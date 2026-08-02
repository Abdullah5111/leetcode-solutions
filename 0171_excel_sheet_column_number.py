"""
171. Excel Sheet Column Number  (Easy)

Time:  O(n)
Space: O(1)
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord("A") + 1)
        return result


if __name__ == "__main__":
    assert Solution().titleToNumber("A") == 1
    assert Solution().titleToNumber("AB") == 28
    assert Solution().titleToNumber("ZY") == 701
    assert Solution().titleToNumber("Z") == 26
    assert Solution().titleToNumber("AA") == 27
    print("ok")
