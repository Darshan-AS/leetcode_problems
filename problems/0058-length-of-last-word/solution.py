class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j = len(s) - 1
        char_found = False
        for i in range(len(s) - 1, -1, -1):
            if not char_found and s[i] != ' ':
                char_found = True
                j = i
                
            if char_found and s[i] == ' ':
                return j - i
        return j + 1 if s and s[0] != ' ' else 0
            
