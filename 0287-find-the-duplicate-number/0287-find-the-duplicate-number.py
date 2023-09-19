class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Approach: Fast and Slow Pointers (Floyd's Cycle Detection Algorithm)
        
        # initialize pointers
        slow = nums[0]
        fast = nums[0]
        
        # move pointers. loop terminates when cycle is detected
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        # the duplicate element is at the start of the cycle. to find it, reset "slow" and move both pointers 1 step at a time. They will meet at the start of the cycle.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
                
        return slow
        
        