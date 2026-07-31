"""
2864. Maximum Odd Binary Number  (Easy)

Time:  O(n)
Space: O(n)  (for the output)
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        zeros = len(s) - ones
        return "1" * (ones - 1) + "0" * zeros + "1"


if __name__ == "__main__":
    assert Solution().maximumOddBinaryNumber("010") == "001"
    assert Solution().maximumOddBinaryNumber("0101") == "1001"
    assert Solution().maximumOddBinaryNumber("1") == "1"
    assert Solution().maximumOddBinaryNumber("111") == "111"
    print("ok")
