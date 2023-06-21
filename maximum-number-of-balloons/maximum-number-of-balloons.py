from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_counts = defaultdict(int)
        for c in text:
            text_counts[c] += 1
            
        numBalloons = 0
        while True:
            for c in "balloon":
                if c in text_counts:
                    text_counts[c] -= 1
                    if text_counts[c] == 0:
                        del text_counts[c]
                else:
                    return numBalloons
            numBalloons += 1
        return numBalloons
            
        
        