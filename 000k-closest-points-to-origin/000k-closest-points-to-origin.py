import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Approach: Maintain a maxHeap of size k. Iterate over the points (x_i, y_i), and add the tuple (distance, x_i, y_i) to the heap, and if the size of the heap exceeds k, then pop out the point furthest away. At the end, we'll end up with the k closest points to the origin.
        
        maxHeap = []
        for i in range(len(points)):
            x, y = points[i]
            d = math.sqrt(x**2 + y**2)
            
            heapq.heappush(maxHeap, (-d, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
                
        return [[x, y] for _, x, y in maxHeap]
        