class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        
        # Helper function to return a list of the neighbors of an index (the indices that we can jump to, as long as it's within bounds)
        def getNeighborIndices(index):
            neighbors = []
            for neighbor in [index + arr[index], index - arr[index]]:
                if 0 <= neighbor < n:
                    neighbors.append(neighbor)
            
            return neighbors
        
        # Run DFS starting at "start" until you hit the element 0
        def dfs(index):
            # returns True if the element 0 can be reached from 'index'
            if arr[index] == 0:
                self.answer = True
            
            if self.answer:
                return True
            
            for neighbor in getNeighborIndices(index):
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
            
            return self.answer
        
        self.answer = False
        visited = {start}
        return dfs(start)