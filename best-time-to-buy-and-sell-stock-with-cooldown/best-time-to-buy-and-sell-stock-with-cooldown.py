class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach: Bottom-up DP
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]
        
        # base case is implicitly programmed
        
        for i in range(n-1,-1,-1):
            for holding in [0,1]:
                skip = dp[i+1][holding]
                if holding == True:
                    # sell the stock
                    transaction = prices[i] + dp[i+2][0]
                else:
                    # buy the stock
                    transaction = -prices[i] + dp[i+1][1]
                
                dp[i][holding] = max(skip, transaction)
                
        return dp[0][0]
        
#         # Approach: Top-down DP
        
#         # The helper function dp(i, holding) returns the maximum profit that can be obtained from day 'i' onwards, if we are currently holding stock (True/False)
#         @cache
#         def dp(i, holding):
#             # base case
#             if i >= n:
#                 return 0
            
#             # Recurrence relation
#             skip = dp(i+1, holding)
#             if holding == True:
#                 # sell the stock
#                 transaction = prices[i] + dp(i+2, False)
#             else:
#                 # buy the stock
#                 transaction = -prices[i] + dp(i+1, True)
                
#             return max(skip, transaction)
        
#         n = len(prices)
#         return dp(0, False)