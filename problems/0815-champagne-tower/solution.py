class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        return min(list(reduce(
            lambda row, _: map(sum, pairwise(
                chain((0,), (max(x - 1, 0) / 2 for x in row), (0,))
            )),
            range(query_row),
            (poured,),
        ))[query_glass], 1)
        
