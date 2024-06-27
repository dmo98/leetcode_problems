class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        r = 1
        while r < numRows:
            inner_list = [0 for i in range(len(result[r-1]) + 1)]
            for i in range(len(inner_list)):
                if i == 0:
                    inner_list[i] = result[r-1][i]
                elif i == len(inner_list) - 1:
                    inner_list[i] = result[r-1][i-1]
                else:
                    inner_list[i] = result[r-1][i] + result[r-1][i-1]
                    
            result.append(inner_list)
            # print(inner_list)
            r += 1
        return result
            
        
        