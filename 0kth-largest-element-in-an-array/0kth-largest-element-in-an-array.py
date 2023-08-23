import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach: maintain a minHeap of size k. At each step, push the new value into the minHeap, pop the smallest value from the minHeap. At the end, we'll have the k'th largest element at the root of the minHeap
        minHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
        