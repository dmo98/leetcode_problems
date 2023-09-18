class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Approach: Top-down DP. 
        
        # The helper function dp(i, holding) returns the maximum profit that can be achieved from day 'i' onwards if we are currently holding stock (True/False).
        @cache
        def dp(i, holding):
            # base case
            if i >= len(prices):
                return 0
            
            # Recurrence relation
            skip = dp(i+1, holding)
            if holding == False:
                # buy stock
                transaction = -prices[i] + dp(i+1, True)
            else:
                # sell stock and pay transaction fee
                transaction = prices[i] - fee + dp(i+1, False)
                
            return max(skip, transaction)
        
        return dp(0, False)
        
        