class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def jump(index: int):
            return (
                min(map(jump, range(index + 1, index + nums[index] + 1)), default=math.inf) + 1
                if index < len(nums) - 1
                else 0
            )
        
        return jump(0)
