class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # two pointer approach
        i = 0
        j = len(nums) - 1
        result = nums[:]
        k = len(nums) - 1
        while i < j:
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i]**2
                i += 1
            else:
                result[k] = nums[j]**2
                j -= 1
            k -= 1
            
        if i == j:
            result[k] = nums[i]**2
        return result
        
        # # trivial approach
        # squared_nums = [num**2 for num in nums]
        # squared_nums.sort()
        # return squared_nums
        