from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Better solution: O(n) time, O(n) space
        balloon_counts = defaultdict(int)
        text_counts = defaultdict(int)
        for c in "balloon":
            balloon_counts[c] += 1
        for c in text:
            text_counts[c] += 1
            
        numBalloons = float('inf')
        for c in "balloon":
            numBalloons = min(numBalloons, text_counts[c] // balloon_counts[c])
        return numBalloons
#         # Brute Force using HashMap: O(m*n) time, O(n) space
#         text_counts = defaultdict(int)
#         for c in text:
#             text_counts[c] += 1
            
#         numBalloons = 0
#         while True:
#             for c in "balloon":
#                 if c in text_counts:
#                     text_counts[c] -= 1
#                     if text_counts[c] == 0:
#                         del text_counts[c]
#                 else:
#                     return numBalloons
#             numBalloons += 1
#         return numBalloons
            
        
        