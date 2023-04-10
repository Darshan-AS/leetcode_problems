class Solution:
    def isValid(self, s: str) -> bool:
        pairs = defaultdict(str, ('()', '{}', '[]'))
        stack = ['']
        for c in s:
            if c in pairs: stack.append(c)
            elif pairs[stack[-1]] == c: stack.pop()
            else: return False
        return len(stack) == 1
            
