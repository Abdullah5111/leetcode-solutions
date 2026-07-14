"""
2169. Count Operations to Obtain Zero  (Easy)

You are given two non-negative integers `num1` and `num2`. In one operation, if
num1 >= num2 you subtract num2 from num1, otherwise you subtract num1 from num2.
Return the number of operations required to make either num1 or num2 equal to 0.

Approach: repeatedly subtracting the smaller value from the larger is exactly
the subtractive Euclidean algorithm. Instead of looping one subtraction at a
time (slow when one number is much larger), subtract in bulk: from the larger
value we can remove the smaller one floor(larger / smaller) times at once. Add
that many operations and continue with the remainder.

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
