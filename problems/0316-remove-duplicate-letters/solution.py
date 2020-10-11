from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = Counter(s)
        
        used = set()
        stack = []
        for ch in s:
            remaining[ch] -= 1
            if ch in used:
                continue
            
            while stack and (x := stack[-1]) > ch and remaining[x] > 0:
                stack.pop()
                used.remove(x)
            stack.append(ch)
            used.add(ch)
            print(stack)
        
        return ''.join(stack)
                
