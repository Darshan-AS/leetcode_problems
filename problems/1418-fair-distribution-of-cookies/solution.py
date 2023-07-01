class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        average = sum(cookies) // k

        def min_unfairness(i: int, kids: list[int], zero_count: int) -> int:
            if i == len(cookies): return max(kids)
            unfairness = inf

            if len(cookies) - i < zero_count: return unfairness # Prune if #cookies_left < #kids_with_zero
            optimal_next_kids = filter(lambda j: kids[j] < average, range(len(kids))) # Prune if kid_j has more cookies than average

            for j in optimal_next_kids:
                is_kid_j_zero = int(kids[j] == 0)
                
                kids[j] += cookies[i]
                unfairness = min(unfairness, min_unfairness(i + 1, kids, zero_count - is_kid_j_zero))
                kids[j] -= cookies[i]
            
            return unfairness
        
        return min_unfairness(0, [0] * k, k)
