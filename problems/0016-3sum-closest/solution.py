class Solution:
    def threeSumClosest(self, nums: list[int], target_: int) -> int:
        def two_sum_closest(seq: list[int], target: int, start: int=0, end: int = None):
            end = end if end is not None else len(seq)
            
            closest_sum = math.inf
            left, right = start, end - 1
            while left < right:
                sum_ = seq[left] + seq[right]
                
                if target > sum_:
                    left += 1
                elif target < sum_:
                    right -= 1
                else:
                    return target
                
                closest_sum = min((closest_sum, sum_), key=lambda x: abs(target - x))
            return closest_sum
        
        def k_sum_closest(seq: list[int], target: int, k: int, start: int=0, end: int = None):
            end = end if end else len(seq)
            if (s := sum(seq[ :k])) >= target: return s
            if (s := sum(seq[-k:])) <= target: return s
            if k == 2: return two_sum_closest(seq, target, start, end)
            
            closest_sums = (
                seq[i] + k_sum_closest(seq, target - seq[i], k - 1, i + 1, end)
                for i in range(start, end - k + 1)
            )
            
            return min(closest_sums, key=lambda x: abs(x - target), default=math.inf)
        
        
        return k_sum_closest(sorted(nums), target_, 3)

