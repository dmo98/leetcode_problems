import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        # Approach: at each step, add the two sticks of minimum length, and keep track of the total cost. We can efficiently find the minimum length sticks by converting the array to a minHeap
        
        # converts the array to a minHeap
        heapq.heapify(sticks) 
        
        total_cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            
            total_cost += first + second
            
            heapq.heappush(sticks, first + second)
            
        return total_cost