"""
134. Gas Station  (Medium)

There are n gas stations along a circular route, where the amount of gas
at the i-th station is gas[i]. You have a car with an unlimited gas tank
and it costs cost[i] of gas to travel from the i-th station to the next
one. Return the starting gas station's index if you can travel around
the circuit once in the clockwise direction, otherwise return -1.
The solution is guaranteed to be unique.

Approach: if total gas >= total cost a start exists; greedily reset the
start to the station after any point where the running tank goes negative.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = tank = start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1
                tank = 0
        return start if total >= 0 else -1


if __name__ == "__main__":
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert Solution().canCompleteCircuit([5], [4]) == 0
    assert Solution().canCompleteCircuit([3, 1, 1], [1, 2, 2]) == 0
    print("ok")
