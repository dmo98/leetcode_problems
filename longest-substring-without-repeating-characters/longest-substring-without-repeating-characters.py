from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use sliding window approach with hashmap
        left = 0
        answer = 0
        counts = defaultdict(int)
        for right in range(len(s)):
            counts[s[right]] += 1
            
            while counts[s[right]] > 1:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            
            answer = max(answer, right - left + 1)
        return answer