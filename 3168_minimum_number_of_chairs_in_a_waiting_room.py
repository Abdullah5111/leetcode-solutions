"""
3168. Minimum Number of Chairs in a Waiting Room  (Easy)

You are given a string `s` describing events in a waiting room, simulated from
an empty room. 'E' means a person enters and takes a chair; 'L' means a person
leaves and frees a chair. Return the minimum number of chairs needed so that
every entering person has a chair at every point in time.

Approach: track the current number of people in the room as we replay the
events ('E' → +1, 'L' → -1). The answer is the peak occupancy reached, since we
need at least that many chairs to cover the busiest moment.

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
