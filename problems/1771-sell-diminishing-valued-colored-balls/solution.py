class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        n_sum = lambda n: n * (n + 1) // 2
        count_balls = lambda counts, k: sum(c - k for c in counts if c > k)
            
        low, high = 0, max(inventory)
        while low < high:
            mid = (low + high) // 2
            max_orders = count_balls(inventory, mid)
            
            if max_orders < orders:
                high = mid
            elif max_orders > orders:
                low = mid + 1
            else:
                low = high = mid
        
        M = 1_000_000_007
        return (
            sum((n_sum(i) - n_sum(low)) % M for i in inventory if i > low) % M +
            (low * (orders - count_balls(inventory, low))) % M
        ) % M
