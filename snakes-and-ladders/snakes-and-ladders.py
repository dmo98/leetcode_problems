from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Firstly, we need to implement a helper function that can locate the (r,c) coordinates for a number in the Boustrophedon style grid.
        
        def findCoordinates(num):
            row = n - 1 - ((num-1)//n)
            if num % n == 0:
                col = n - 1
            else:
                col = (num % n) - 1
            if ((num-1) // n) % 2 == 1:
                col = n - 1 - col
            return row, col
            
        # Second, run BFS starting at 1, adding neighbors in the range [curr+1 -> min(curr+6, n^2)] to the queue. If grid cell is a snake or ladder, relocate to the correct location. Stop BFS when you reach n^2 and return the minimum number of steps needed.
        
        n = len(board)
        
        queue = deque([1])
        visited = {1}
        steps = 0
        
        while len(queue) != 0:
            num_nodes = len(queue)
            
            for _ in range(num_nodes):
                node = queue.popleft()
                # stopping criteria for BFS
                if node == n**2:
                    return steps
                
                for neighbor in range(node+1, min(node+6, n**2)+1):
                    r, c = findCoordinates(neighbor)
                    if board[r][c] == -1:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                    else:
                        new_num = board[r][c]
                        if new_num not in visited:
                            visited.add(new_num)   
                            queue.append(new_num)
            
            steps += 1
            
        return -1
                    
        