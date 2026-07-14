"""
2264. Largest 3-Same-Digit Number in String  (Easy)

You are given a string `num` representing a large integer. An integer is good if
it is a substring of `num` with length 3 and all its digits are the same. Return
the maximum good integer as a string, or "" if none exists. Note the answer may
have leading zeros (e.g. "000").

Approach: scan every length-3 window. A window is good when its three characters
are equal. Track the largest good string seen. Since all good strings have the
same length, ordinary string comparison ranks them correctly.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                triple = num[i : i + 3]
                if triple > best:
                    best = triple
        return best


if __name__ == "__main__":
    assert Solution().largestGoodInteger("6777133339") == "777"
    assert Solution().largestGoodInteger("2300019") == "000"
    assert Solution().largestGoodInteger("42352338") == ""
    assert Solution().largestGoodInteger("999999999") == "999"
    print("ok")
