class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0
        
        for ch in s:
            if ch == '(':
                low, high = low + 1, high + 1
            elif ch == ')' and high:
                low, high = max(low - 1, 0), high - 1
            elif ch == '*':
                low, high = max(low - 1, 0), high + 1
            else: return False
        
        return low == 0
                
