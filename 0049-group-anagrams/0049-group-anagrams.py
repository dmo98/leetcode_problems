from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            counts = [0]*26 # array that contains count of each character from a - z
            for c in s:
                counts[ord(c) - ord('a')] += 1
                
            hashmap[tuple(counts)].append(s)
            
        answer = []    
        for key in hashmap.keys():
            answer.append(hashmap[key])
        return answer
        
        
#         # O(n * mlogm) time, O(n*m) space,
#         # where n = number of strings in 'strs' and m = avg. length of a string
#         hashmap = defaultdict(list)
#         for s in strs:
#             key = "".join(sorted(s))
#             hashmap[key].append(s)
            
#         answer = []
#         for key in hashmap.keys():
#             answer.append(hashmap[key])
#         return answer