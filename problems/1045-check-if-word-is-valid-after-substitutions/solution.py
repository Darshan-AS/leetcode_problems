class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch in 'ab':
                stack.append(ch)
            elif not (len(stack) >= 2 and stack.pop() + stack.pop() == 'ba'):
                return False
        
        return not stack
                
