import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Approach: Run binary search on the solution space to get the minimum possible divisor. The solution space is [1, max(nums)].The task is possible if the sum of division results (rounded up) is <= threshold 
        
        # helper function to check if task is possible
        def check(divisor):
            result = 0
            for i in range(len(nums)):
                result += math.ceil(nums[i] / divisor)
                
            return result <= threshold
        
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                # search for a better solution
                right = mid - 1
            else:
                left = mid + 1
                
        return left 
            