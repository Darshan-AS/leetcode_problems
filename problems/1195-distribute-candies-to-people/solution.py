from math import sqrt

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n_dist = (sqrt(4 * 2 * candies + 1) - 1) // 2 # Number of sequential distributions
        q, r = divmod(n_dist, num_people)
        
        def get_candies_for(i):
            k = q + 1 if q * num_people + i <= n_dist else q
            return int(k * i + (k - 1) * k * num_people // 2)
            
        ans = list(map(get_candies_for, range(1, num_people + 1)))
        ans[int(n_dist % num_people)] += candies - int(n_dist * (n_dist + 1) // 2)
        return ans
