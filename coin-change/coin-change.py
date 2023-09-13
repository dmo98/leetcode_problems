class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Approach: Use backtracking with memoization. The helper function takes as argument the remaining amount. At each node in the tree, consider all neighbors (entire array 'coins'), and only expand branches to those children where the child doesn't exceed the remaining amount, prune the other ones. Base case: the remaining amount == 0.
        
        def backtrack(rem_amount):
            """
            This helper function returns the minimum number of coins needed to sum upto the remaining amount
            """
            # base case
            if rem_amount == 0:
                return 0
            
            # if the sub-tree was already explored somewhere else (in order to not repeat the same computation)
            if rem_amount in memo:  
                return memo[rem_amount]
            
            minCoins = float("inf")
            for num in coins:
                if num > rem_amount:  # prune branch 
                    continue
                    
                numCoins = backtrack(rem_amount - num) # recursive call
                
                if numCoins == -1:
                    continue # prune branch that doesn't sum upto amount
                minCoins = min(minCoins, 1 + numCoins)
                
            if minCoins == float("inf"): # no child was explored -> dead end
                memo[rem_amount] = -1
                return -1
                
            memo[rem_amount] = minCoins    
            return minCoins
           
        memo = {}
        minCoins = backtrack(amount)
        
        return minCoins
            