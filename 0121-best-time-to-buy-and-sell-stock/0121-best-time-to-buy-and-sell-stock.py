class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        # DP approach: TLE
        def dp(i, bought=False):
            # Returns the max profit that can be obtained from day i onwards
            
            # base case
            if i >= len(prices):
                return 0
            
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            # recurrence relation:
            # On day i, we have 2 decisions: buy/sell stock or skip
            if not bought:
                buy = -prices[i] + dp(i+1, True)
                skip = dp(i+1, bought)
                memo[(i, bought)] = max(buy, skip)
            else:
                sell = prices[i]
                skip = dp(i+1, bought)
                memo[(i, bought)] = max(sell, skip)
            return memo[(i, bought)]
        
        memo = {}
        return dp(0, 0)