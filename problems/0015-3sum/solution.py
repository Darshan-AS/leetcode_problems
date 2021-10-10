class Solution:
    def threeSum(self, nums_: List[int]) -> List[List[int]]:        
        def two_sum(nums, target, start=0, end=None):
            end = end if end else len(nums)
            seen = set()
            for num in nums[start:end]:
                if target - num in seen:
                    yield (num, target - num)
                else:
                    seen.add(num)
        
        def three_sum(nums, target, start=0, end=None):
            end = end if end else len(nums)
            for i in range(start, end):
                yield from (s + (nums[i],) for s in two_sum(nums, target - nums[i], start=i + 1))
        
        return set(map(lambda s: tuple(sorted(s)), three_sum(nums_, 0)))
