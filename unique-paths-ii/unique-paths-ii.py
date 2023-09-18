class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Approach: Top-down DP

        # The helper function dp(row, col) returns the number of unique paths from (0,0) -> (row, col) without hitting any obstacles.
        @cache
        def dp(row, col):
            # base case: dp(0,0) = 1 (if it's not an obstacle)
            if row == 0 and col == 0:
                if obstacleGrid[row][col] == 0:
                    return 1
                else:
                    return 0
            
            if obstacleGrid[row][col] == 1 or row < 0 or col < 0: # obstacle present or out of bounds
                return 0
            
            # Recurrence relation
            return dp(row-1,col) + dp(row, col-1)
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dp(m-1, n-1)