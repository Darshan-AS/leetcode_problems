class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        count = k
        
        for i in num:
            while count and stack and i < stack[-1]:
                stack.pop()
                count -= 1
            
            if stack or i != "0":
                stack.append(i)
                
        while stack and count:
            stack.pop()
            count -= 1
            
        return ''.join(stack) if stack else "0"
