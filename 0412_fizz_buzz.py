"""
412. Fizz Buzz  (Easy)

Given an integer `n`, return a string array `answer` (1-indexed) where:
  * answer[i] == "FizzBuzz" if i is divisible by both 3 and 5,
  * answer[i] == "Fizz"     if i is divisible by 3,
  * answer[i] == "Buzz"     if i is divisible by 5,
  * answer[i] == str(i)     otherwise.

Approach: iterate from 1 to n. Build each entry by appending "Fizz" when the
number is divisible by 3 and "Buzz" when divisible by 5; if neither applies, use
the number's string form. Concatenating handles the FizzBuzz case automatically.

Time:  O(n)
Space: O(n)  (for the output)
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            word = ""
            if i % 3 == 0:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
            answer.append(word or str(i))
        return answer


if __name__ == "__main__":
    assert Solution().fizzBuzz(3) == ["1", "2", "Fizz"]
    assert Solution().fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert Solution().fizzBuzz(15)[-1] == "FizzBuzz"
    assert Solution().fizzBuzz(1) == ["1"]
    print("ok")
