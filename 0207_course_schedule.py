"""
207. Course Schedule  (Medium)

There are numCourses courses labeled 0 to numCourses - 1 and a list
prerequisites where prerequisites[i] = [a, b] means you must take b
before a. Return true if you can finish all courses (i.e. the
prerequisite graph has no cycle).

Approach: Kahn's topological sort — repeatedly take courses with
indegree 0 and decrement dependents; a cycle leaves leftover courses.

Time:  O(V + E)
Space: O(V + E)
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for nxt in adj[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses


if __name__ == "__main__":
    assert Solution().canFinish(2, [[1, 0]]) is True
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
    assert Solution().canFinish(4, [[1, 0], [2, 1], [3, 2]]) is True
    assert Solution().canFinish(1, []) is True
    print("ok")
