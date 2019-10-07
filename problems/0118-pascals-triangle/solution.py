class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        if numRows == 0:
            return triangle
        
        triangle.append([1])
        for _ in range(1, numRows):
            prev = triangle[-1]
            
            next = [prev[i] + prev[i + 1] for i in range(len(prev) - 1)]
            triangle.append([1] + next + [1])
        
        return triangle
