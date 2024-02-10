class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        # Two Pointers approach
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]: # it's profitable
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else: # if not profitable, we have found a new low
                left = right
            right += 1
        return max_profit
                
        
        
#         # DP approach: TLE
#         def dp(i, bought=False):
#             # Returns the max profit that can be obtained from day i onwards
            
#             # base case
#             if i >= len(prices):
#                 return 0
            
#             if (i, bought) in memo:
#                 return memo[(i, bought)]
            
#             # recurrence relation:
#             # On day i, we have 2 decisions: buy/sell stock or skip
#             if not bought:
#                 buy = -prices[i] + dp(i+1, True)
#                 skip = dp(i+1, bought)
#                 memo[(i, bought)] = max(buy, skip)
#             else:
#                 sell = prices[i]
#                 skip = dp(i+1, bought)
#                 memo[(i, bought)] = max(sell, skip)
#             return memo[(i, bought)]
        
#         memo = {}
#         return dp(0, 0)