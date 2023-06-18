class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # Prefix Sum approach
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        result = []
        for i in range(len(nums)):
            if i < k or i > len(nums)-k-1:
                result.append(-1)
            else:
                k_radius_ave = (prefix[i+k] - prefix[i-k] + nums[i-k])//(2*k+1)
                result.append(k_radius_ave)
        return result
        