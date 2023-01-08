class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        Pair = tuple[float, float]

        def line_eqn(p1: Pair, p2: Pair) -> Pair:
            (x1, y1), (x2, y2) = p1, p2

            m = (y2 - y1) / (x2 - x1) if x2 != x1 else math.inf
            c = y1 - m * x1 if x2 != x1 else math.inf
            return m, c
        
        n = len(points)
        cs = (Counter(line_eqn(points[i], points[j]) for j in range(i + 1, n)) for i in range(n - 1))
        return max((c.most_common(1)[0][1] for c in cs), default=0) + 1
