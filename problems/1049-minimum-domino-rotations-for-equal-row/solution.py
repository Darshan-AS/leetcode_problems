from collections import Counter

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a = Counter(A).most_common(1)[0]
        b = Counter(B).most_common(1)[0]
        
        solution_row, option_row, target = (A, B, a[0]) if a[1] > b[1] else (B, A, b[0])
        count = 0
        for i, j in zip(solution_row, option_row):
            if i != target and j != target: return -1
            count += 0 if i == target else 1
        return count
