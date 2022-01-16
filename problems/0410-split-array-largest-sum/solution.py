class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        
        @cache
        def minimized_largest_sum(i: int, k: int) -> int:
            if k == 1: return prefix_sums[-1] - prefix_sums[i]
            
            n = len(nums)
            minimum_largest_split_sum = prefix_sums[-1]
            for j in range(i, n - (k - 1)):
                head_split_sum = prefix_sums[j + 1] - prefix_sums[i]
                
                if head_split_sum >= minimum_largest_split_sum: # Prune
                    continue
                
                tail_minimum_largest_split_sum = minimized_largest_sum(j + 1, k - 1)
                
                minimum_largest_split_sum = min(
                    minimum_largest_split_sum,
                    max(head_split_sum, tail_minimum_largest_split_sum),
                )
            
            return minimum_largest_split_sum
                
            # # Without pruning
            # return min(
            #     max(prefix_sums[j + 1] - prefix_sums[i], minimized_largest_sum(j + 1, k - 1))
            #     for j in range(i, len(nums) - (k - 1))
            # ) if k > 1 else (prefix_sums[-1] - prefix_sums[i])
        
        return minimized_largest_sum(0, m)
