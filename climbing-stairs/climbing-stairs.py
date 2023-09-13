class Solution:
    def climbStairs(self, n: int) -> int:
        # Approach: Top-down DP
        
        def dp(i):
            # This helper function returns the number of distinct ways to climb to the i'th step
            
            # Base cases: i = 0 or 1
            if i <= 1:
                return 1
            
            if i in memo:
                return memo[i]
            
            # Recurrence relation
            memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        
        memo = {}
        return dp(n)
            
        