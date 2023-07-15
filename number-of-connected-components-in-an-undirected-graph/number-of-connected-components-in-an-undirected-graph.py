from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # construct the graph by maintaining a hashmap that maps nodes to a list of it's neighbors. Iterate over all the nodes, if it hasn't been seen till now, run DFS starting at that node and increment count (since the new CC started here).
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        # construct the graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        # count the number of connected components
        cc = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                dfs(i)
                cc += 1
        
        return cc