class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Approach: Use backtracking. The helper function takes the array of numbers being built, the current sum of the numbers, as well as "start", which is the number to start iterating from (to determine valid child nodes). Base case -> nums.length == k and sum(nums) == n. 
        
        def backtrack(nums, current_sum, start):
            if len(nums) == k and current_sum == n:
                answer.append(nums[:])
                return
            
            for child_node in range(start, 10):
                if current_sum + child_node > n or len(nums) > k:  # abandon path
                    continue
                    
                nums.append(child_node)
                current_sum += child_node
                backtrack(nums, current_sum, child_node+1)
                nums.pop()
                current_sum -= child_node
            
        answer = []
        backtrack([], 0, 1)
        return answer
        