# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq

class Solution:

    """
    Runtime 1047 ms Beats 5.00%
    """
    def floyd_warshall(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u][v] = w
        
        for m in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == j:
                        continue
                    graph[i][j] = min(graph[i][j], graph[i][m] + graph[m][j])
        answer = -1
        cnt = 0
        for w in graph[k]:
            if w == float('inf'):
                continue
            answer = max(answer, w)
            cnt += 1

        return answer if cnt >= n - 1 else -1

    """
    Runtime 387 ms Beats 31.42%
    """
    def bfs(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, k)]
        visited = set()
        answer = 0

        while pq:
            time, node = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)
            answer = max(answer, time)

            for v, w in graph[node]:
                if v in visited:
                    continue
                heapq.heappush(pq, (time + w, v))

        return answer if len(visited) == n else -1