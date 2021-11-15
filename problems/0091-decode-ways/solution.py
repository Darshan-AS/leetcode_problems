class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def num_decodings(index: int) -> int:
            if index >= len(s): return 1
            if int(s[index]) == 0: return 0
            
            return num_decodings(index + 1) + (
                num_decodings(index + 2)
                if index + 2 <= len(s) and int(s[index: index + 2]) <= 26 
                else 0
            )
        
        return num_decodings(0)
