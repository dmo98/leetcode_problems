class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Sliding Window approach
        left = 0
        total = 0
        for right in range(k):
            total += nums[right]
            
        result = total
        for right in range(k, len(nums)):
            total = total + nums[right] - nums[right-k]
            result = max(result, total)
        return result/k
        
        