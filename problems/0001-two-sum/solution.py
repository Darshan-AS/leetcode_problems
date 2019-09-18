class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map.keys():
                return hash_map[nums[i]], i
            hash_map[target - nums[i]] = i
