class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = -1
        seen = {}
        for index, char in enumerate(s):
            if char in seen:
                start = max(start, seen[char])
            max_length = max(max_length, index - start)
            seen[char] = index
        return max_length 
