class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def min_days_to_ship(weights: list[int], capacity: int) -> int:
            return reduce(
                lambda a, x: (a[0] + 1, x) if a[1] + x > capacity else (a[0], a[1] + x),
                weights,
                (1, 0), # (no_of_days, weights_on_current_day)
            )[0]
        
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            d = min_days_to_ship(weights, m)
            l, r = (l, m) if d <= days else (m + 1, r)
        return r
