from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        
        for c in s:
            d1[c] += 1
            
        for c in t:
            d2[c] += 1
            
        for key in d1:
            if d1[key] != d2[key]:
                return False
        return True