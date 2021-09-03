class Solution:
    def BFS(self, grid, i, j):
        """ TRIED USING BFS: Time Limit Exceeded
        queue = [(i,j)]
        while queue != []:
            i,j = queue[0][0], queue[0][1]
            for (x,y) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if x<0 or x>=len(grid) or y<0 or y>=len(grid[i]):
                    pass
                else:
                    if grid[x][y] == '1':
                        queue.append((x,y))
            grid[i][j] = 0
            queue.pop(0)      
        """
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[i]):
            return None
        if grid[i][j] != '1':
            return None
        grid[i][j] = '2'
        self.BFS(grid, i-1, j)
        self.BFS(grid, i+1, j)
        self.BFS(grid, i, j-1)
        self.BFS(grid, i, j+1)
        
            
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.BFS(grid, i, j)
                    islands += 1
        return islands
                