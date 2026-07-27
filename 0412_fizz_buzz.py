"""
412. Fizz Buzz  (Easy)

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
