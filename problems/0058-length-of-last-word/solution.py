class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        
        i = len(s) - 1
        while i >= 0 and s[i] == ' ': i -= 1
        
        last_length = 0
        while i >= 0 and s[i] != ' ':
            last_length += 1
            i -= 1
        
        return last_length
