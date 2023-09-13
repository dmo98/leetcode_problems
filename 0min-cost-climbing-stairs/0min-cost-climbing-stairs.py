class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach: Top-down DP
        
        def dp(i):
            # helper function returns the minimum cost to reach the i'th step.
            
            # base cases: dp[0] = dp[1] = 0
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            # Recurrence relation
            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))
        