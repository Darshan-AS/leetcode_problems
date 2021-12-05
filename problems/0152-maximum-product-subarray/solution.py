class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_min = lambda xs: (max(xs), min(xs))
        
        return max(islice(accumulate(
            nums,
            lambda a, x: max_min((a[0] * x, x, a[1] * x)), 
            initial=(1, 1),
        ), 1, None))[0]
