class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        pos_max = neg_max = 1
        
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                pos_max, neg_max = neg_max + 1, neg_max
            elif nums[i - 1] > nums[i]:
                pos_max, neg_max = pos_max, pos_max + 1
        
        return max(pos_max, neg_max)
