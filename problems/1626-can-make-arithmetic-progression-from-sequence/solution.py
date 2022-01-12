class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        def is_arithmetic(iterable: iter) -> bool:
            a, b = tee(iterable)
            next(a, None)
            return len(set(map(operator.sub, a, b))) == 1
        
        return is_arithmetic(sorted(arr))
