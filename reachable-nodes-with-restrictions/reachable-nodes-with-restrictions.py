from collections import defaultdict

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # construct the graph by creating a hashmap that maps nodes to a list of it's neighbors. Then, run DFS starting at node 0, ignoring nodes on the restricted list and keeping track of the number of non-restricted nodes that can be reached.
        
        # construct the graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        
        def dfs(node):
            # this helper function performs DFS on the graph starting at "node", ignoring the nodes on the restricted list, and returns the number of non-restricted nodes that can be reached.
            
            result = 1
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    seen.add(neighbor)
                    result += dfs(neighbor)
            
            return result
            
        # run DFS starting at node 0
        seen = {0}
        restricted = set(restricted) # enables O(1) checking for existence
        return dfs(0)
        
            
        