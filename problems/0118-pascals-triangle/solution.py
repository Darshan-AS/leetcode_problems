from itertools import chain

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        def pascals_triangle():
            level = (1,)
            while True:
                yield level
                level = tuple(chain((1,), (level[i] + level[i + 1] for i in range(len(level) - 1)), (1,)))
        
        return list(itertools.islice(pascals_triangle(), n))
