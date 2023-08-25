from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Approach: At each step, greedily remove the most frequent element until the size of the array is halved.
        
        counter = Counter(arr)
        size = len(arr)
        
        maxHeap = [-value for value in counter.values()]
        heapq.heapify(maxHeap)
        
        minSetSize = 0
        while True:
            if size <= len(arr)/2:
                break
                
            value = -heapq.heappop(maxHeap)
            size -= value
            minSetSize += 1
            
        
        return minSetSize