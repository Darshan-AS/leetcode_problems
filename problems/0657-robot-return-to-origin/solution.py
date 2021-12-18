class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        
        def simulate(pos: tuple[int, int], move: str) -> tuple[int, int]:
            x, y = pos
            dx, dy = move_map[move]
            return x + dx, y + dy
        
        init_pos = (0, 0)
        return reduce(simulate, moves, init_pos) == init_pos
