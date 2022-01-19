class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Similar to problem 678
        low, high = 0, 0
        
        for ch in map(lambda c, l: c if l == '1' else '*', s, locked):
            if ch == '(':
                low, high = low + 1, high + 1
            elif ch == ')' and high:
                low, high = max(low - 1, 0), high - 1
            elif ch == '*':
                low, high = max(low - 1, 0), high + 1
            else: return False
        
        return low == high % 2 == 0
