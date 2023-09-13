class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Approach: Bottom-up DP
        n = len(cost)
        dp = [0] * (n+1)
        # base cases are implicitly included: dp[0]=dp[1]=0
        
        for i in range(2,len(cost)+1):
            # Recurrence relation
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return dp[n]
        
#         # Approach: Top-down DP
        
#         def dp(i):
#             # helper function returns the minimum cost to reach the i'th step.
            
#             # base cases: dp[0] = dp[1] = 0
#             if i <= 1:
#                 return 0
            
#             if i in memo:
#                 return memo[i]
            
#             # Recurrence relation
#             memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
#             return memo[i]
        
#         memo = {}
#         return dp(len(cost))
        