from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # construct the graph by maintaining a hashmap that maps nodes to a list of it's neighbors. Run DFS starting at the source, if we run into destination, return True otherwise return False
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if neighbor == destination:
                        break
                    dfs(neighbor)
        
        # construct the graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        # run DFS starting at source
        seen = {source}
        dfs(source)
        
        return (destination in seen)
        
        