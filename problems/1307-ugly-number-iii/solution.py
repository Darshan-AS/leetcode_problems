class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm = cache(math.lcm)
        
        # Count of ugly numbers in [1, k]
        le_count = lambda k: (
            (k // a + k // b + k // c) - 
            (k // lcm(a, b) + k // lcm(b, c) + k // lcm(c, a)) + 
            (k // lcm(a, b, c))
        )
        
        low, high = 1, 2 * 10 ** 9
        while low < high:
            mid = (low + high) // 2
            count = le_count(mid)
            
            if   count < n: low  = mid + 1
            elif count > n: high = mid - 1
            else          : high = mid
            
        return low
            
