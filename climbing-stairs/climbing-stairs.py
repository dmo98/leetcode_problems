from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach: Bottom-up DP. Can improve space complexity to O(1) since recurrence relation is static, by storing last two values in variables instead of the entire table.
        dp = [1] * (n+1)
        
        # base cases are implicit: dp[0] = dp[1] = 1
        for i in range(2,n+1):
            # Recurrence relation
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
    
#         # Approach: Top-down DP
#         @cache
#         def dp(i):
#             # This helper function returns the number of distinct ways to climb to the i'th step
            
#             # Base cases: i = 0 or 1
#             if i <= 1:
#                 return 1
            
#             # Recurrence relation
#             return dp(i-1) + dp(i-2)
        
#         return dp(n)

            
        