class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        
        def evaluate(a, op, b):
            return a + b if op == '+' else a - b
        
        i = 0
        stack = []
        while i < len(s):
            if s[i] in ('+', '-', '('):
                stack.append(s[i])
                i += 1
            elif s[i] == ')' and len(stack) > 2:
                b = stack.pop()
                stack.pop()
                op = stack.pop()
                a = stack.pop()
                stack.append(evaluate(a, op, b))
                i += 1
            elif s[i].isdigit():
                a = 0
                while i < len(s) and s[i].isdigit():
                    a = a * 10 + int(s[i])
                    i += 1

                if stack and stack[-1] in ('+', '-'):
                    op = stack.pop()
                    stack.append(evaluate(stack.pop(), op, a))
                else:
                    stack.append(a)
            else:
                i += 1
        
        return stack.pop()
