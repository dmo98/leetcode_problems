class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # keep track of max
        maxVal = -float('inf')
        maxInd = -1
        for i in range(len(nums)):
            if nums[i] > maxVal:
                maxVal = nums[i]
                maxInd = i
        
        # compare to other elements
        for i in range(len(nums)):
            if maxVal < 2 * nums[i] and i != maxInd:
                return -1
        return maxInd
        