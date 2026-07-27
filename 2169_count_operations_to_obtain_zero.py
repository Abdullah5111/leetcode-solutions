"""
2169. Count Operations to Obtain Zero  (Easy)

Time:  O(log(max(num1, num2)))
Space: O(1)
"""

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ops = 0
        while num1 and num2:
            if num1 >= num2:
                ops += num1 // num2
                num1 %= num2
            else:
                ops += num2 // num1
                num2 %= num1
        return ops


if __name__ == "__main__":
    assert Solution().countOperations(2, 3) == 3
    assert Solution().countOperations(10, 10) == 1
    assert Solution().countOperations(0, 5) == 0
    assert Solution().countOperations(5, 0) == 0
    print("ok")
