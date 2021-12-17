class Solution:
    def getAverages(self, nums_: List[int], k: int) -> List[int]:
        def window_sums(nums: list[int], w: int):
            n = len(nums)
            if w > n: return
            
            curr_sum = 0
            for i in range(n):
                curr_sum += nums[i]
                if i == w - 1:
                    yield curr_sum
                elif i > w - 1:
                    curr_sum -= nums[i - w]
                    yield curr_sum
        
        n = len(nums_)
        k_ = 2 * k + 1
        if k_ > n: return [-1] * n
        return [-1] * k + list(map(lambda x: x // k_, window_sums(nums_, k_))) + [-1] * k
        
        
        
