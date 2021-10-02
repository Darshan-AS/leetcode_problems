class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {open_b: close_b for open_b, close_b in ("()", "{}", "[]")}
        open_brackets = set(bracket_pairs.keys())
        
        stack = []
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            elif stack and bracket_pairs[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        
        return not stack
