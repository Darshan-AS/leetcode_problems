class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def get_next_row(prev_row: Iterable[int]):
            yield 1
            for i in range(len(prev_row) - 1):
                yield prev_row[i] + prev_row[i + 1]
            yield 1
        
        row = (1,)
        yield row
        for _ in range(numRows - 1):
            row = tuple(get_next_row(row))
            yield row
