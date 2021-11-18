class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        def line_eqn(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            
            m = (y2 - y1) / (x2 - x1) if x2 != x1 else math.inf
            c = y1 - m * x1 if x2 != x1 else math.inf
            return m, c 
        
        max_points = 1
        for i in range(n - 1):
            max_points = max(
                max_points, 
                Counter(
                    line_eqn(points[i], points[j])
                    for j in range(i + 1, n)
                ).most_common(1)[0][1] + 1
            )
        
        return max_points
