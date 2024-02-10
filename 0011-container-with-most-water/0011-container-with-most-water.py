class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two Pointers approach
        maxArea = 0
        left = 0
        right = len(height)-1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea
        
        # # Brute-force approach: double loop 
        # # O(n*2) time, O(1) space -> TLE
        # maxArea = 0
        # for i in range(0, len(height)-1):
        #     for j in range(i+1, len(height)):
        #         area = min(height[i], height[j]) * (j-i)
        #         maxArea = max(maxArea, area)
        # return maxArea
        