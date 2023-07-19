from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Implement a helper funtion to return a list of valid neighbors of a gene string. A neighbor of a gene string is another gene string that is identical except at 1 position, and it's valid if it's in the bank
        def getNeighbors(gene):
            neighbors = []
            for candidate in bank:
                diff = 0
                for i in range(len(gene)):
                    if gene[i] != candidate[i]:
                        diff += 1
                
                if diff == 1:
                    neighbors.append(candidate)
                
            return neighbors
        
        # Run BFS starting at startGene until you hit reach endGene, counting the number of steps/mutations it takes. Keep track of the visited gene strings in a set.
        
        visited = {startGene}
        queue = deque([startGene])
        numMutations = 0
        
        while len(queue) != 0:
            print(queue)
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                gene = queue.popleft()
                if gene == endGene:
                    return numMutations
                
                for neighbor in getNeighbors(gene):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
            numMutations += 1
        
        return -1
                        