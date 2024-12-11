# https://leetcode.com/problems/course-schedule/

class Solution:

    """
    Runtime 4 ms Beats 69.63%
    """
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        done = set()
        table = dict()

        for c, p in prerequisites:
            table.setdefault(c, []).append(p)

        def dfs(course):
            if not course in table or not table[course]:
                return True
            if course in done:
                return False

            done.add(course)
            for c in table[course]:
                if not dfs(c):
                    return False
            table[course] = []
            return True
        
        for c in table.keys():
            if not dfs(c):
                return False

        return True