class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Approach: Use a hashmap to keep track of character counts in 's'. Iterate over characters in 't', if present in hashmap then decrement count else return the character.
        
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
            
        for c in t:
            if c in counts:
                counts[c] -= 1
                if counts[c] == 0:
                    del counts[c]
                
            else:
                return c
        