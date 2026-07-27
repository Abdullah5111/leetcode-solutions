"""
3895. Count Digit Occurrences  (Easy)

Time:  O(total digits)
Space: O(1)  (ignoring the per-number string)
"""

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        target = str(digit)
        count = 0
        for n in nums:
            for ch in str(n):
                if ch == target:
                    count += 1
        return count


if __name__ == "__main__":
    assert Solution().countDigitOccurrences([12, 23, 34], 3) == 2
    assert Solution().countDigitOccurrences([111], 1) == 3
    assert Solution().countDigitOccurrences([50, 30, 20], 0) == 3
    assert Solution().countDigitOccurrences([12], 9) == 0
    assert Solution().countDigitOccurrences([0], 0) == 1
    print("ok")
