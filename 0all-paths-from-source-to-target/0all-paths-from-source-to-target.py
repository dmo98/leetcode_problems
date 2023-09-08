class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Approach: Use backtracking. Helper function takes path as argument, which is the current path being built. Base case -> last node in path is the target (n-1), then append path to the answer array.
        
        def backtrack(path):
            if path[-1] == n-1: # reached the target
                all_paths.append(path[:])
                return
            
            # otherwise, make recursive calls to it's neighbors
            node = path[-1]
            for neighbor in graph[node]:
                path.append(neighbor)
                backtrack(path)
                path.pop()
                
        n = len(graph)
        all_paths = []
        backtrack([0])
        return all_paths
                
            
        
        
        