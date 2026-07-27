"""
2264. Largest 3-Same-Digit Number in String  (Easy)

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
