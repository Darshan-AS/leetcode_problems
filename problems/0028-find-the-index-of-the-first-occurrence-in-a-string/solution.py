class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            j, k = 0, i
            while k < len(haystack) and j < len(needle) and haystack[k] == needle[j]:
                k += 1
                j += 1
            
            if j == len(needle):
                return k - len(needle)
        
        return -1
        
        
