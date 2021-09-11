class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """ O(n^2): Time Limit Exceeded
        if len(nums) == 1:
            return nums[0]
        subarrays = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                subarrays.append(sum(nums[i:j]))
            subarrays.append(sum(nums[i:]))
        print(subarrays)
        return max(subarrays)
        """
        if len(nums) == 1:
            return nums[0]
        
        prefix_sum = nums[0]
        largest_sum = nums[0]
        for num in nums[1:]:
            if num > prefix_sum and prefix_sum < 0:
                prefix_sum = num
            else:
                prefix_sum = prefix_sum + num
            
            if prefix_sum > largest_sum:
                largest_sum = prefix_sum
        return largest_sum