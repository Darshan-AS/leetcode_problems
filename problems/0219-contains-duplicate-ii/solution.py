class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k: return False
        
        window = set(nums[:k])
        if len(window) < min(len(nums), k):
            return True
            
        for i in range(k, len(nums)):
            if nums[i] in window:
                return True
            window.remove(nums[i - k])
            window.add(nums[i])
        return False
