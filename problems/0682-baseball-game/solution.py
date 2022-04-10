class Solution:
    def calPoints(self, ops: list[str]) -> int:
        score_stack = []
        
        for op in ops:
            match op:
                case '+': score_stack.append(score_stack[-2] + score_stack[-1])
                case 'D': score_stack.append(score_stack[-1] * 2)
                case 'C': score_stack.pop()
                case  s : score_stack.append(int(s))
        
        return sum(score_stack)
