class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        prefix_sums = islice(accumulate(nums, operator.add, initial=0), n)
        suffix_sums = islice(accumulate(nums, operator.sub, initial=sum(nums)), 1, None)
                
        for i, p_sum, s_sum in zip(range(n), prefix_sums, suffix_sums):
            if p_sum == s_sum: return i
        return -1
