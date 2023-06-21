from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Use HashMap to keep track of counts
        dic = defaultdict(int)
        for c in magazine:
            dic[c] += 1
            
        for c in ransomNote:
            if c in dic:
                dic[c] -= 1
                if dic[c] == 0:
                    del dic[c]
            else:
                return False
        return True