import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Use Two Heap approach: left subarray (first k elements in decreasing order) should be a minHeap and right subarray (remaining n-k elements) should be a maxHeap
        nums_sorted = sorted(nums, reverse=True)
        self.minHeap, self.maxHeap = nums_sorted[:k], nums_sorted[k:]
        self.maxHeap = [-val for val in self.maxHeap]   # to simulate a maxHeap
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)      
        self.k = k

    def add(self, val: int) -> int:
        # edge case : if there aren't at least k numbers passed into the constructor
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            
        # if val < KthLargest, push to maxHeap
        elif val < self.minHeap[0]:
            heapq.heappush(self.maxHeap, -val)
        
        # otherwise, push to minHeap, pop from minHeap (since minHeap would have k+1 elements), and push this value to the maxHeap
        else:
            heapq.heappush(self.minHeap, val)
            x = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -x)
            
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)