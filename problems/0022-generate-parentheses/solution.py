class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def parens(n: int) -> Iterator[str]:
            yield from (
                '(' + ins + ')' + outs
                for i in range(n)
                for ins in parens(i)
                for outs in parens(n - i - 1)
            ) if n else ('',)
        
        return list(parens(n))
