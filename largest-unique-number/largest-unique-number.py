from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Using a HashMap to store counts of numbers
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        maxUniqueNum = -1
        for num in counts.keys():
            if counts[num] == 1 and num > maxUniqueNum:
                maxUniqueNum = num
        return maxUniqueNum
        