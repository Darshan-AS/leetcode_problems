class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        start_cell, final_cell = 1, n * n

        def dest(cell: int) -> int:
            q, r = divmod(cell - 1, n)
            return board[-q - 1][-r - 1 if q % 2 else r]
        
        seen = {start_cell}
        queue = deque(((start_cell, 0),))
        while queue:
            label, move = queue.popleft()
            for i in range(min(label + 6, final_cell), label, -1):
                next_label = i if (d := dest(i)) == -1 else d

                if next_label == final_cell: return move + 1

                if next_label not in seen:
                    seen.add(next_label)
                    queue.append((next_label, move + 1))
        
        return -1
