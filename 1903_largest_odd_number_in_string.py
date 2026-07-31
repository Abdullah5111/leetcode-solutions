"""
1903. Largest Odd Number in String  (Easy)

Time:  O(n)
Space: O(1)
"""


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[: i + 1]
        return ""


if __name__ == "__main__":
    assert Solution().largestOddNumber("52") == "5"
    assert Solution().largestOddNumber("4206") == ""
    assert Solution().largestOddNumber("35427") == "35427"
    assert Solution().largestOddNumber("0214683") == "0214683"
    assert Solution().largestOddNumber("2") == ""
    print("ok")
