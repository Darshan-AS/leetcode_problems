class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = Counter(moves)
        return c['R'] == c['L'] and c['U'] == c['D']
