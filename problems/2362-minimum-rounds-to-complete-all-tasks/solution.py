class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        def min_rounds(n: int) -> int:
            match divmod(n, 3):
                case q, 0: return q
                case q, 1: return q + 1 if q else -1
                case q, 2: return q + 1
        
        rounds = map(min_rounds, Counter(tasks).values())
        return reduce(lambda a, x: -1 if -1 in (a, x) else a + x, rounds)
