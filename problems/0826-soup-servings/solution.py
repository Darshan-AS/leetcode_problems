class Solution:
    probs = []

    def soupServings(self, n: int) -> float:
        m, k = ceil(n / 25), len(self.probs)
        self.probs.extend(takewhile(
            lambda x: x <= 1 - 1e-5,
            (self.empty_prob(i, i) for i in range(k, m + 1))
        ))
        return self.probs[m if m < k else -1]
    
    @cache
    def empty_prob(self, a: int, b: int) -> float:
        match a <= 0, b <= 0:
            case True , True : return 0.5
            case True , False: return 1.0
            case False, True : return 0.0
            case False, False: return sum(
                self.empty_prob(a - da, b - db)
                for da, db in ((4, 0), (3, 1), (2, 2), (1, 3)) 
            ) / 4
