class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        return list(accumulate(
            range(num_rows - 1),
            lambda a, _: [1, *map(sum, pairwise(a)), 1],
            initial=[1],
        ))
        
