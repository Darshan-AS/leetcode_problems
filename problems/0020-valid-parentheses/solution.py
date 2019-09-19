class Solution:
    def isValid(self, s: str) -> bool:
        braces_pair = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        stack = []
        for i in s:
            if i in braces_pair.keys():
                stack.append(i)
            elif i in braces_pair.values() and stack and braces_pair[stack[-1]] == i:
                stack.pop()
            else:
                return False
        
        return not stack
