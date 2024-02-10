from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            
        # this array stores index:value mapping, where index = frequency of a number, and value = list containing all the numbers that occur as many times as the index value
        frequencies = [[]] * (len(nums) + 1) # starting from index 0 to index len(nums)
        for num, count in hashmap.items():
            frequencies[count] = frequencies[count] + [num]
            
        # retrieve the k most frequent numbers
        top_k_most_freq = []
        index = len(frequencies)-1
        while index >= 0:
            candidates = frequencies[index]
            while len(candidates) > 0 and k > 0:
                value = candidates.pop()
                top_k_most_freq.append(value)
                k -= 1
            
            if k == 0:
                break
                
            index -= 1
        
        return top_k_most_freq
        
#         # O(nlogn) time, O(n) space
#         hashmap = defaultdict(int)
#         for num in nums:
#             hashmap[num] += 1
            
#         top_k_freq = sorted(set(nums), key=lambda num:hashmap[num], reverse=True)[:k]
#         return top_k_freq