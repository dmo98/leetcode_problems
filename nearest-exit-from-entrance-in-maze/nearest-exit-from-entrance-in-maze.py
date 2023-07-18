from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # run BFS starting at the entrance, counting the steps it takes to reach an exit (which is a boundary cell that isn't the entrance), else if there is no exit return -1
        
        m = len(maze)
        n = len(maze[0])
        
        def isValidCell(row, col):
            if (0 <= row < m) and (0 <= col < n) and maze[row][col] == '.':
                return True
            return False
        
        neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = deque([tuple(entrance)])
        visited = {tuple(entrance)}
        steps = 0
        
        while len(queue) != 0:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                row, col = queue.popleft()
                
                # if we have reached an exit, return the number of steps
                if (row, col) != tuple(entrance) and (row == 0 or row == m-1 or col == 0 or col == n-1):
                    return steps
                    
                # add neighbors to the queue
                for dx, dy in neighbors:
                    new_row, new_col = row + dx, col + dy
                    if (new_row, new_col) not in visited and isValidCell(new_row, new_col):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            
            steps += 1
                            
        # if path not found
        return -1
        
        
        