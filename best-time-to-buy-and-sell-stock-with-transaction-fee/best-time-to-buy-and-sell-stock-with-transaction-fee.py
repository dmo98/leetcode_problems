class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach: Top-down DP. 
        
        # The helper function dp(i, holding) returns the maximum profit that can be achieved from day 'i' onwards if we are currently holding stock (True/False).
        def dp(i, holding):
            # base case
            if i >= len(prices):
                return 0
            
            if (i, holding) in memo:
                return memo[(i, holding)]
            
            # Recurrence relation
            skip = dp(i+1, holding)
            if holding == False:
                # buy stock
                transaction = -prices[i] + dp(i+1, True)
            else:
                # sell stock and pay transaction fee
                transaction = prices[i] - fee + dp(i+1, False)
                
            memo[(i, holding)] = max(skip, transaction)
            return memo[(i, holding)]
        
        memo = {}
        return dp(0, False)
        
        