class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        m = len(mat)
        n = len(mat[0])
        r, c = 0, 0     # start at index (0, 0)

        if m > 1 and n > 1:
            direction = 'right'
            while 0 <= r <= m-1 and 0 <= c <= n-1: 
                output.append(mat[r][c])
                if direction == 'right':
                    c += 1
                    if r == 0:
                        direction = 'diag-down'
                    elif r == m-1:
                        direction = 'diag-up'
                elif direction == 'down':
                    r += 1
                    if c == 0:
                        direction = 'diag-up'
                    elif c == n-1:
                        direction = 'diag-down'
                elif direction == 'diag-up':
                    r -= 1
                    c += 1
                    if c == n-1:
                        direction = 'down'
                    elif r == 0:
                        direction = 'right'
                elif direction == 'diag-down':
                    r += 1
                    c -= 1
                    if r == m-1:
                        direction = 'right'
                    elif c == 0:
                        direction = 'down'
        
        elif m == 1:
            direction = 'right'
            while 0 <= c <= n-1:
                output.append(mat[r][c])
                c += 1
        elif n == 1:
            direction = 'down'
            while 0 <= r <= m-1:
                output.append(mat[r][c])
                r += 1
        
        return output
                