class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        
        for index, ch in enumerate(s):
            if count[ch] == 1:
                return index    
        return -1
