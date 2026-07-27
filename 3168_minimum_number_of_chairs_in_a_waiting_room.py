"""
3168. Minimum Number of Chairs in a Waiting Room  (Easy)

Time:  O(n)
Space: O(1)
"""

class Solution:
    def minimumChairs(self, s: str) -> int:
        current = 0
        peak = 0
        for event in s:
            if event == "E":
                current += 1
                peak = max(peak, current)
            else:
                current -= 1
        return peak


if __name__ == "__main__":
    assert Solution().minimumChairs("EEEEEEE") == 7
    assert Solution().minimumChairs("ELELEEL") == 2
    assert Solution().minimumChairs("ELEELEELLL") == 3
    print("ok")
