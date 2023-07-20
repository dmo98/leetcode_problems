from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # The problem is identical to the one that asks for the size of the largest connected component.
        
        # helper function to determine if b2 is in range of b1
        def inRange(b1, b2):
            x1, y1, r1 = b1
            x2, y2, r2 = b2
            
            if math.sqrt((x2-x1)**2 + (y2-y1)**2) <= r1:
                return True
            return False
        
        # Create the graph in hashmap format, mapping each node/bomb to a list of it's neighbors (all bombs within range)
        numBombs = len(bombs)
        
        graph = defaultdict(list)
        for i in range(numBombs):
            for j in range(numBombs):
                if i == j:  # skip
                    continue
                
                b1, b2 = bombs[i], bombs[j]
                # check if b2 in range of b1. If yes -> b2 is a neighbor of b1
                if inRange(b1, b2):
                    x1, y1, r1 = b1
                    x2, y2, r2 = b2
                    
                    graph[(x1, y1, r1, i)].append((x2, y2, r2, j))
 

        # helper function for running DFS on a node, keeping track of the size of the connected component.
        def dfs(node):
            x, y, r, i = node
            answer = 1  # counting the bomb itself
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    answer += dfs(neighbor)
            return answer
        
        # Iterate over all nodes/bombs, run DFS starting at each node and keep track of the max bombs detonated
        maxBombsDetonated = 0
        
        for i in range(numBombs):
            x, y, r = bombs[i]
            visited = {(x,y,r,i)}
            bombsDetonated = dfs((x,y,r,i))
             
            maxBombsDetonated = max(bombsDetonated, maxBombsDetonated)
        
        
        return maxBombsDetonated
            
                    