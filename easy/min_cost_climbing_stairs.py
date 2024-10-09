# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:

    """
    Runtime 46 ms Beats 94.12%
    """
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        
        return dp[-1]