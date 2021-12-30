class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:        
        max_i_sums = accumulate(starmap(operator.add, enumerate(values)), max, initial=0) # prefix sums
        return max(i_sum + j_val - j for i_sum, (j, j_val) in zip(max_i_sums, enumerate(values)))
