# https://leetcode.com/problems/course-schedule-ii/

from collections import defaultdict

class Solution:
    """
    Runtime 3 ms Beats 78.40%
    """
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        table = defaultdict(list)
        indegree = [0] * numCourses
        queue = []
        answer = []

        for c, p in prerequisites:
            table[c].append(p)
            indegree[p] += 1
        
        for i, v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        
        while queue:
            course = queue.pop(0)

            for pre in table[course]:
                indegree[pre] -= 1
                if indegree[pre] == 0:
                    queue.append(pre)
            answer.append(course)

        if len(answer) != numCourses:
            return []
        return list(reversed(answer))