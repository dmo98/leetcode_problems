class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Prefix Sum approach
        prefix = [nums[0]]
        min_prefix_sum = nums[0]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
            min_prefix_sum = min(min_prefix_sum, prefix[-1])
            
        if min_prefix_sum < 1:
            return 1 - min_prefix_sum
        else:
            return 1
            
        
        