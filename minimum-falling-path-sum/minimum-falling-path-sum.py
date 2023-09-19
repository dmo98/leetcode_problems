class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Approach: Top-down DP
        
        def inBounds(r, c):
            if (0 <= r < m) and (0 <= c < n):
                return True
            return False
        
        # the helper function dp(row, col) returns the minimum falling path sum from r = 0 -> r = row
        @cache
        def dp(row, col):
            # base case
            if row == 0:
                return matrix[row][col]
            
            answer = matrix[row][col]
            neighbors = float("inf")
            if inBounds(row-1,col):
                neighbors = min(neighbors, dp(row-1,col))
            if inBounds(row-1,col-1):
                neighbors = min(neighbors, dp(row-1,col-1))
            if inBounds(row-1,col+1):
                neighbors = min(neighbors, dp(row-1,col+1))
                
            if neighbors == float("inf"):
                neighbors = 0
            return answer + neighbors
        
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 1:
            return min(matrix[0])
        
        answer = float("inf")
        for c in range(n):
            answer = min(answer, dp(m-1,c))
        return answer