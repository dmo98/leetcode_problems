class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monotonic_dec = True
        monotonic_inc = True
        i = 1
        while i < len(nums):
            if not monotonic_inc and not monotonic_dec:
                return False
            
            if nums[i] > nums[i-1] and monotonic_dec == True:
                monotonic_dec = False
            
            if nums[i] < nums[i-1] and monotonic_inc == True:
                monotonic_inc = False
                
            i += 1
            
        if not monotonic_inc and not monotonic_dec:
            return False
            
        # either monotone increasing or monotone decreasing
        return True
        