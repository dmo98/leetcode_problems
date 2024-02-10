from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            
        top_k_freq = sorted(set(nums), key=lambda num:hashmap[num], reverse=True)[:k]
        return top_k_freq