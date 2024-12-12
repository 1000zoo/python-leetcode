# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict

class Solution:

    """
    Runtime 0 ms Beats 100.00%
    """
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)
        for eq, value in zip(equations, values):
            graph[eq[0]].append((eq[1], value))
            graph[eq[1]].append((eq[0], 1/value))
        
        def bfs(source, target):
            if not (source in graph and target in graph):
                return -1

            queue = [(source, 1)]
            visited = set()

            while queue:
                curr_var, curr_value = queue.pop(0)
                if curr_var in visited:
                    continue
                visited.add(curr_var)
                for variable, value in graph[curr_var]:
                    temp = curr_value * value
                    if variable == target:
                        return temp
                    queue.append((variable, temp))

            return -1
        
        return [bfs(s, t) for s, t in queries]
