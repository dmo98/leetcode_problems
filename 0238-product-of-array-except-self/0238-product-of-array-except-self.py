from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # maps index i to product of first numbers upto (and including) index i 
        prefixProd = defaultdict(int)
        prefixProd[0] = nums[0]
        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i-1] * nums[i]
        # maps index i to product of ending numbers from (including) index i
        suffixProd = defaultdict(int)
        suffixProd[len(nums)-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i]
            
        answer = []
        for i in range(len(nums)):
            if i >= 1:
                prefix = prefixProd[i-1]
            else:
                prefix = 1
                
            if i <= len(nums)-2:
                suffix = suffixProd[i+1]
            else:
                suffix = 1
            
            answer.append(prefix * suffix)
        return answer