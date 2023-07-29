class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n / 25)
        return self.empty_prob(m, m) if m < 200 else 1.0
    
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
