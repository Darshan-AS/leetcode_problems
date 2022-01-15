class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t, tc = max(Counter(tops).items(), key=lambda c: c[1])
        b, bc = max(Counter(bottoms).items(), key=lambda c: c[1])
        
        xs, ys, k, kc = (tops, bottoms, t, tc) if tc > bc else (bottoms, tops, b, bc)
        return len(xs) - kc if all(x == k or y == k for x, y in zip(xs, ys)) else -1
