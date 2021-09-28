from itertools import chain, product
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_seq(seq: Iterable) -> bool:
            return all(1 <= int(k) <= 9 and v == 1 for k, v in Counter(filter(lambda ch: ch != '.', seq)).items())

        def rows(matrix: List[List]) -> Iterable[Iterable]:
            yield from map(iter, matrix)

        def cols(matrix: List[List]) -> Iterable[Iterable]:
            yield from map(iter, zip(*matrix))

        def sub_matrices(matrix: List[List], sm: int, sn: int) -> Iterable[Iterable]:
            m, n = len(matrix), len(matrix[0])
            if m % sm or n % sn: return
            for i, j in product(range(0, m, sm), range(0, n, sn)):
                yield (matrix[i][j] for i, j in product(range(i, i + sm), range(j, j + sn)))

        return (
            all(map(is_valid_seq, rows(board)))
            and all(map(is_valid_seq, cols(board)))
            and all(map(is_valid_seq, sub_matrices(board, 3, 3)))
        )
