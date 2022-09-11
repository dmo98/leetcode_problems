class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        elementCounts = {}
        for i in range(len(nums)):
            if nums[i] not in elementCounts:
                elementCounts[nums[i]] = 0
            elementCounts[nums[i]] += 1
        
        for num in elementCounts.keys():
            if elementCounts[num]%2 == 1:
                return False
            
        return True
        