class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        # # Sliding Window approach
        # left = 0
        # diff = 0 
        # maxDiff = 0
        # for right in range(len(prices)):
            
            
        
        
        # DP approach: TLE
        @cache
        def dp(i, bought=False):
            # Returns the max profit that can be obtained from day i onwards
            
            # base case
            if i >= len(prices):
                return 0
            
            # recurrence relation:
            # On day i, we have 2 decisions: buy/sell stock or skip
            if not bought:
                buy = -prices[i] + dp(i+1, True)
                skip = dp(i+1, bought)
                return max(buy, skip)
            else:
                sell = prices[i]
                skip = dp(i+1, bought)
                return max(sell, skip)
        
        return dp(0, 0)