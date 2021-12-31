from itertools import chain

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        def pairwise(iterable):
            a, b = tee(iterable)
            next(b, None)
            return zip(a, b)
        
        def pascals_triangle():
            level = (1,)
            while True:
                yield level
                level = (1, *starmap(operator.add, pairwise(level)), 1)
        
        return list(islice(pascals_triangle(), n))
