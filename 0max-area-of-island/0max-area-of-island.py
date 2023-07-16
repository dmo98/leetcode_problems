class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # the problem basically asks for the size of the largest connected component
        # Approach: iterate over each grid cell, if the cell is a part of an island that hasn't been visited, run DFS on it. During DFS, keep track of the number of cells that make up the island. Keep track of the max island size and return it.
        
        m = len(grid)
        n = len(grid[0])
        
        def isValid(row, col):
            if (0 <= row < m) and (0 <= col < n) and grid[row][col] == 1:
                return True
            return False
        
        def dfs(row, col):
            # returns the size of the connected component that the cell at (row, col) belongs to
            area = 1
            
            for dx, dy in adjacent_cells:
                new_row, new_col = row + dx, col + dy
                if isValid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    area += dfs(new_row, new_col)
                
            return area
                        
        
        seen = set()
        maxArea = 0
        adjacent_cells = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    area = dfs(row, col)
                    maxArea = max(area, maxArea)
        
        return maxArea
        