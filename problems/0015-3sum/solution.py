class Solution:
    def threeSum(self, nums_: List[int]) -> List[List[int]]:  
        def two_sum(nums, target, start=0, end=None):
            end = end if end else len(nums)
            
            left, right = start, end - 1
            while left < right:
                sum_ = nums[left] + nums[right]
                
                if target > sum_ or (left > start and nums[left] == nums[left - 1]):
                    left += 1
                elif target < sum_ or (right < end - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    yield (nums[left], nums[right])
                    left += 1
                    right -= 1
                    
        
        def three_sum(nums, target, start=0, end=None):
            end = end if end else len(nums)
            for i in range(start, end):
                if i > 0 and nums[i] == nums[i - 1]: continue
                num1 = nums[i]
                yield from ((num1, num2, num3) for num2, num3 in two_sum(nums, target - num1, start = i + 1))
        
        return list(three_sum(sorted(nums_), 0))
