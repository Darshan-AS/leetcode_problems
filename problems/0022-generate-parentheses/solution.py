class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def parens(k: int, score: int, ps: list):
            if not k and not score:
                yield ''.join(ps)
                return
            
            if not k or score > n: return
            
            for b in '()' if score else '(':
                ps.append(b)
                new_score = score + 1 if b == '(' else score - 1
                yield from parens(k - 1, new_score, ps)
                ps.pop()
        
        return list(parens(2 * n, 0, []))
