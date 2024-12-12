# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from collections import defaultdict
import heapq

class Solution:


    """
    Runtime 0 ms Beats 100.00%
    """
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        queue = [(0, src)] # price, node
        costs = [float('inf') for _ in range(n)]

        while k >= 0 and queue:
            iter_num = len(queue)
            for _ in range(iter_num):
                curr_cost, curr_node = queue.pop(0)
                
                for next_node, next_cost in graph[curr_node]:
                    temp = curr_cost + next_cost

                    if costs[next_node] > temp:
                        costs[next_node] = temp
                        queue.append((temp, next_node))
            
            k -= 1

        return -1 if costs[dst] == float('inf') else costs[dst]


    """
    Runtime 99 ms Beats 16.94%
    """
    def bfs(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        pq = [(0, 0, src)] # total_price, depth, node
        best = dict()
        answer = float('inf')

        while pq:
            price, depth, node = heapq.heappop(pq)
            
            if node == dst:
                return min(answer, price)
            if depth > k:
                continue
            if (node, depth) in best and best[(node, depth)] <= price:
                continue
            best[(node, depth)] = price
            for neighbor, np in graph[node]:
                heapq.heappush(pq, (price + np, depth + 1, neighbor))


        return -1
            

    """
    Time Limit Exceeded
    """
    def depth_first_search(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        def dfs(curr, depth, cost):
            if depth > k:
                return float('inf')
            if curr == dst:
                return cost
            ans = float('inf')
            for neighbor, price in graph[curr]:
                temp = price + cost
                ans = min(ans, dfs(neighbor, depth + 1, temp))
            return ans
        answer = dfs(src, -1, 0)
        if answer == float('inf'):
            return -1
        return answer
            


