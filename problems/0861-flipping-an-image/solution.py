class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [list(map(lambda x: int(x == 0), reversed(row))) for row in A]
