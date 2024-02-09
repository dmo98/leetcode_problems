from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            hashmap[key].append(s)
            
        answer = []
        for key in hashmap.keys():
            answer.append(hashmap[key])
        return answer