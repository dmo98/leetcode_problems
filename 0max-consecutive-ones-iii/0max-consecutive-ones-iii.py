class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """ This problem is the same as trying to find the longest subarray that contains at most k zeros"""
        # Sliding Window approach
        left = 0
        zero_count = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
                
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            max_length = max(max_length, right-left+1)
        return max_length
        
        