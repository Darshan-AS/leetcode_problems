class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def can_jump(index: int):
            return (
                any(map(can_jump, range(index + 1, index + nums[index] + 1)))
                if index < len(nums) - 1
                else True
            )
        
        return can_jump(0)
