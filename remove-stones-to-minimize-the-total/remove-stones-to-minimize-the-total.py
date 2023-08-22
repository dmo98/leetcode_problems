import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Approach: During each operation, take the max pile, and halve it. We can repeatedly get the max pile by converting the array into a maxHeap.
        
        maxHeap = [-val for val in piles]  # to simulate as a maxHeap
        heapq.heapify(maxHeap)
        
        i = 0
        while i < k:
            val = abs(heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, -(val - (val//2)))
            
            i += 1
            
        return -sum(maxHeap)
        
        