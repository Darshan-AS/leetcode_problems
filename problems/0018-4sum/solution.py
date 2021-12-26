class Solution:
    def fourSum(self, nums: List[int], target_: int) -> List[List[int]]:
        def k_sum(seq: Sequence[int], target: int, k: int, start=0, end=None):
            end = end if end else len(seq)
            
            if k == 1:
                yield from ((target,),) if target in seq[start: end] else ()
                return
            
            for i in range(start, end):
                if i > start and seq[i] == seq[i - 1]: continue
                x = seq[i]
                yield from ((x,) + xs for xs in k_sum(seq, target - x, k - 1, start=i + 1))
        
        return list(k_sum(sorted(nums), target_, 4))
