class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        hash_map = {}
        
        i = 0
        for j in range(len(s)):
            if s[j] in hash_map.keys():
                i = max(hash_map[s[j]] + 1, i)
            hash_map[s[j]] = j
            max_count = max(max_count, j - i + 1)
        
        return max_count
