class Solution:
    def fourSum(self, nums: List[int], target_: int) -> List[List[int]]:
        def two_sum(seq: Sequence[int], target: int, start=0, end=None):
            end = end if end else len(seq)
            
            left, right = start, end - 1
            while left < right:
                sum_ = seq[left] + seq[right]
                
                if target > sum_ or (left > start and seq[left] == seq[left - 1]):
                    left += 1
                elif target < sum_ or (right < end - 1 and seq[right] == seq[right + 1]):
                    right -= 1
                else:
                    yield (seq[left], seq[right])
                    left += 1
                    right -= 1
                    
        def k_sum(seq: Sequence[int], target: int, k: int, start=0, end=None):
            end = end if end else len(seq)
            
            if k == 2:
                yield from two_sum(seq, target, start, end)
                return
            
            for i in range(start, end):
                if i > start and seq[i] == seq[i - 1]: continue
                x = seq[i]
                yield from ((x,) + xs for xs in k_sum(seq, target - x, k - 1, i + 1, end))
        
        return list(k_sum(sorted(nums), target_, 4))
