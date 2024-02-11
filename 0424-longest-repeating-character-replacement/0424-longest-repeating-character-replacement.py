class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window approach
        hashmap = {}
        left = 0
        longestSubstring = 0
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1
            
            while (right-left+1) - max(hashmap.values()) > k:
                # remove elements from the window
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
                
            # resulting window is valid
            longestSubstring = max(longestSubstring, right-left+1)
        return longestSubstring
                