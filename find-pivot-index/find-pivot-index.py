class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0
        for num in nums:
            rightSum += num
        
        for i in range(len(nums)):
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]
        return -1
        