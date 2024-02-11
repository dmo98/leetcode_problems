class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window approach
        hashmap = {}
        left = 0
        current_length = 0
        longest_length = 0
        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1
            
            while hashmap[s[right]] > 1:
                hashmap[s[left]] -= 1
                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]
                left += 1
                
            current_length = right - left + 1
            longest_length = max(longest_length, current_length)
        return longest_length
                
        