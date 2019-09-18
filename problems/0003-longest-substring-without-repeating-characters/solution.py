class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        hash_map = {}
        
        i = 0
        for j, ch in enumerate(s):
            if ch in hash_map.keys():
                i = max(hash_map[ch] + 1, i)
            hash_map[ch] = j
            max_count = max(max_count, j - i + 1)
        
        return max_count
